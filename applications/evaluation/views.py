import os
import json
import pdfkit
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

from django.conf import settings

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string

from .utils import get_plot

from applications.evaluation.models import Evaluation
from .forms import EvaluationDocumentForm




pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')


def generate_base64_plot(fig):
    """Convertit un graphique matplotlib en image base64 pour affichage HTML."""
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    chart_png = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    return chart_png



def view_evaluation(request, patient_id):
    eval = get_object_or_404(Evaluation, id=patient_id)
    form = EvaluationDocumentForm(instance=eval)

    data = Evaluation.objects.all().values()
    df = pd.DataFrame(list(data))

    # Initialisation des graphiques à None
    chart_moyenne = None
    chart_boxplot = None

    if not df.empty:
        # --------- Graphe 1: Moyenne des scores ---------
        fig1 = plt.figure()
        df[['score1', 'score2']].mean().plot(kind='bar')
        plt.title("Moyenne des scores")
        chart_moyenne = generate_base64_plot(fig1)
        plt.close(fig1)

        # --------- Graphe 2: Boxplot ---------
        fig2 = plt.figure()
        df[['score1', 'score3']].mean().plot(kind='bar')
        plt.title("Répartition des scores")
        chart_boxplot = generate_base64_plot(fig2)
        plt.close(fig2)


    html_content = render_to_string(
        'evaluation/pdf_eval.html', {   'eval': eval,
                                        'form': form,
                                        'chart_moyenne': chart_moyenne,
                                        'chart_boxplot': chart_boxplot,
                                    }
    )

    # Indiquer explicitement le chemin vers wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Remplace par le bon chemin

    # Génère le PDF directement en mémoire
    pdf = pdfkit.from_string(html_content, False, configuration=config)

    # Envoie une réponse pour afficher le PDF dans le navigateur sans le sauvegarder
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="dossier_medical_{eval.nom}_{eval.prenom}.pdf"'

    return response



CONFIG_PATH = os.path.join(settings.BASE_DIR, 'config.json')

def charger_chemin_dossier():
    """Charge le chemin du dossier depuis un fichier de config JSON"""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            return config.get("chemin_dossier_patient", "")
    return ""

def enregistrer_chemin_dossier(chemin):
    """Enregistre le chemin du dossier dans un fichier config"""
    with open(CONFIG_PATH, 'w') as f:
        json.dump({"chemin_dossier_patient": chemin}, f)

def export_evaluation(request, patient_id):
     # Adapter si le modèle est ailleurs
    records = Evaluation.objects.filter(id=patient_id)
    if not records.exists():
        return HttpResponse(f"Patient avec l'ID {patient_id} non trouvé.", status=404)


    eval = get_object_or_404(Evaluation, id=patient_id)
    form = EvaluationDocumentForm(instance=eval)

    data = Evaluation.objects.all().values()
    df = pd.DataFrame(list(data))

    data = Evaluation.objects.all().values()
    df = pd.DataFrame(list(data))

    # Initialisation des graphiques à None
    chart_moyenne = None
    chart_boxplot = None


    if not df.empty:
        # --------- Graphe 1: Moyenne des scores ---------
        fig1 = plt.figure()
        df[['score1', 'score2']].mean().plot(kind='bar')
        plt.title("Moyenne des scores")
        chart_moyenne = generate_base64_plot(fig1)
        plt.close(fig1)

        # --------- Graphe 2: Boxplot ---------
        fig2 = plt.figure()
        df[['score1', 'score3']].mean().plot(kind='box')
        plt.title("Répartition des scores")
        chart_boxplot = generate_base64_plot(fig2)
        plt.close(fig2)


    html_content = render_to_string(
        'evaluation/pdf_eval.html', {   'eval': eval,
                                        'form': form,
                                        'chart_moyenne': chart_moyenne,
                                        'chart_boxplot': chart_boxplot,
                                    }
    )

    try:
        pdf = pdfkit.from_string(html_content, False, configuration=pdfkit_config)
    except Exception as e:
        print(f"Erreur lors de la génération du PDF: {str(e)}")
        return HttpResponse(f"Erreur lors de la génération du PDF: {str(e)}", status=500)

    # Charger le chemin d'enregistrement
    dossier_export = charger_chemin_dossier()

    if not dossier_export:
        # Première fois : définir le dossier et l'enregistrer
        dossier_export = os.path.join(settings.MEDIA_ROOT, "pdf_patients")  # Ou n'importe où
        os.makedirs(dossier_export, exist_ok=True)
        enregistrer_chemin_dossier(dossier_export)

    # Nom du fichier
    nom_fichier = f"ListesPatient_{patient_id}.pdf"
    chemin_pdf = os.path.join(dossier_export, nom_fichier)

    # Enregistrement du PDF sur le disque
    with open(chemin_pdf, 'wb') as f:
        f.write(pdf)

    # Réponse HTTP pour téléchargement si tu veux
    with open(chemin_pdf, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{nom_fichier}"'
        return response


def ajouter_eval(request):
    if request.method == 'POST':
        form = EvaluationDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if 'save_and_add' in request.POST:
                return redirect('evaluation_add')  # Reste sur la même page pour une nouvelle évaluation
            else:
                return redirect('evaluation_save')
        else:
            print(form.errors)  # Affiche les erreurs dans le terminal
    else:
        form = EvaluationDocumentForm()
    
    return render(request, 'evaluation/forms_eval.html', {'form': form})


import os
import json
from django.conf import settings
import pdfkit
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from applications.patients_docs.models import ProfilPatient

pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')


def view_medical_record(request, patient_id):
    patient = get_object_or_404(ProfilPatient, id=patient_id)
    
    # Utilise un modèle HTML pour générer le contenu à convertir en PDF
    html_content = render_to_string(
        'patients_docs/pdf_template.html', {'patient': patient}
    )

    # Indiquer explicitement le chemin vers wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Remplace par le bon chemin

    # Génère le PDF directement en mémoire
    pdf = pdfkit.from_string(html_content, False, configuration=config)

    # Envoie une réponse pour afficher le PDF dans le navigateur sans le sauvegarder
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="dossier_medical_{patient.nom}_{patient.prenom}.pdf"'

    return response


# def export_medical_record(request: HttpRequest, patient_id: int) -> HttpResponse:
#     records = ProfilPatient.objects.filter(id=patient_id)

#     if not records.exists():
#         return HttpResponse(f"Patient avec l'ID {patient_id} non trouvé.", status=404)

#     # Assurer que le contexte soit correct et sans espaces dans les clés
#     context = {'dossier_medical': records.first()}  # Utilisation d'un objet unique ici avec 'first()'

#     html = render_to_string('patients_docs/pdf_template.html', context)

#     try:
#         pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)
#     except Exception as e:
#         return HttpResponse(f"Erreur lors de la génération du PDF: {str(e)}", status=500)

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="ListesPatient_{patient_id}.pdf"'

#     return response
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

def export_medical_record(request, patient_id):
     # Adapter si le modèle est ailleurs
    records = ProfilPatient.objects.filter(id=patient_id)

    if not records.exists():
        return HttpResponse(f"Patient avec l'ID {patient_id} non trouvé.", status=404)

    patient = records.first()
    context = {'dossier_medical': patient}
    html = render_to_string('patients_docs/pdf_template.html', context)

    try:
        pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)
    except Exception as e:
        return HttpResponse(f"Erreur lors de la génération du PDF: {str(e)}", status=500)

    # 🔽 Charger le chemin d'enregistrement
    dossier_export = charger_chemin_dossier()

    if not dossier_export:
        # Première fois : définir le dossier et l'enregistrer
        dossier_export = os.path.join(settings.MEDIA_ROOT, "pdf_patients")  # Ou n'importe où
        os.makedirs(dossier_export, exist_ok=True)
        enregistrer_chemin_dossier(dossier_export)

    # 🔽 Nom du fichier
    nom_fichier = f"ListesPatient_{patient_id}.pdf"
    chemin_pdf = os.path.join(dossier_export, nom_fichier)

    # 🔽 Enregistrement du PDF sur le disque
    with open(chemin_pdf, 'wb') as f:
        f.write(pdf)

    # Réponse HTTP pour téléchargement si tu veux
    with open(chemin_pdf, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{nom_fichier}"'
        return response
# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from applications.patients_docs.models import ProfilPatient

# def export_medical_record(request, patient_id):
#     records = ProfilPatient.objects.filter(patient_id=patient_id)

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = f'attachment; filename="dossierpatient{patient_id}.csv"'

#     response.write("Date,Description,Prescription\n")
#     for record in records:
#         response.write(f"{record.date_de_creation_dossier},{record.description},{record.prescription}\n")

#     return response

# from django.shortcuts import render
# import pdfkit
# from django.http import HttpResponse, HttpRequest
# from django.shortcuts import render, get_object_or_404
# from django.template.loader import render_to_string
# from applications.patients_docs.models import ProfilPatient

# # Configuration PDFKit avec le chemin vers wkhtmltopdf


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


def export_medical_record(request: HttpRequest, patient_id: int) -> HttpResponse:
    records = ProfilPatient.objects.filter(id=patient_id)

    if not records.exists():
        return HttpResponse(f"Patient avec l'ID {patient_id} non trouvé.", status=404)

    # Assurer que le contexte soit correct et sans espaces dans les clés
    context = {'dossier_medical': records.first()}  # Utilisation d'un objet unique ici avec 'first()'

    html = render_to_string('patients_docs/pdf_template.html', context)

    try:
        pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)
    except Exception as e:
        return HttpResponse(f"Erreur lors de la génération du PDF: {str(e)}", status=500)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ListesPatient_{patient_id}.pdf"'

    return response

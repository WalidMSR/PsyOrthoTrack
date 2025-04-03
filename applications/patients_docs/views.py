from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from applications.patients_docs.models import ProfilPatient

def export_medical_record(request, patient_id):
    records = ProfilPatient.objects.filter(patient_id=patient_id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="dossierpatient{patient_id}.csv"'

    response.write("Date,Description,Prescription\n")
    for record in records:
        response.write(f"{record.record_date},{record.description},{record.prescription}\n")

    return response
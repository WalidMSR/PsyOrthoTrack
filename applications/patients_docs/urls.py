from django.urls import path
from .views import export_medical_record

urlpatterns = [
    path('export_medical_record/<int:patient_id>/', export_medical_record, name='export_medical_record'),
]
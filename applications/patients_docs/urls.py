from django.urls import path
from . import views

urlpatterns = [
    path('view_medical_record/<int:patient_id>/', views.view_medical_record, name='view_medical_record'),
    path('export_medical_record/<int:patient_id>/', views.export_medical_record, name='export_medical_record'),
]
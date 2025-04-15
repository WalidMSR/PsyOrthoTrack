from django.urls import path
from . import views

urlpatterns = [
    path('view_evaluation/<int:patient_id>/', views.view_evaluation, name='view_evaluation'), 
    path('export_evaluation/<int:patient_id>/', views.export_evaluation, name='export_evaluation'),
    path('ajouter/', views.ajouter_eval, name='ajouter_eval'),
    path('ajouter_evaluation/', views.ajouter_eval, name='evaluation_add'),
    path('', views.ajouter_eval, name='evaluation_save'),
]
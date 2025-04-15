from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_rendezvous, name='liste_rendezvous'),
    path('rendezvous/<int:pk>/', views.detail_rendezvous, name='detail_rendezvous'),
    path('rendezvous/nouveau/', views.creer_rendezvous, name='creer_rendezvous'),
    path('rendezvous/modifier/<int:pk>/', views.modifier_rendezvous, name='modifier_rendezvous'),
    path('rendezvous/supprimer/<int:pk>/', views.supprimer_rendezvous, name='supprimer_rendezvous'),
]

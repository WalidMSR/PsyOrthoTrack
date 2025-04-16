from django.contrib import admin
from .models import RendezVous

class RendezVousAdmin(admin.ModelAdmin):
    list_display = (
        'nom_patient', 'date', 'heure', 'type_seance', 'statut', 
        'teleconsultation', 'prix', 'est_paye'
    )
    list_filter = ('statut', 'type_seance', 'teleconsultation', 'date')
    search_fields = ('nom_patient', 'email', 'description')
    ordering = ('-date', 'heure')
    readonly_fields = ('cree_le', 'modifie_le')
    fieldsets = (
        ("Informations patient", {
            'fields': ('nom_patient', 'telephone', 'email'),
        }),
        ("Détails du rendez-vous", {
            'fields': ('date', 'heure', 'duree', 'type_seance', 'statut', 'teleconsultation'),
        }),
        ("Notes & Paiement", {
            'fields': ('description', 'prix', 'est_paye'),
        }),
        ("Suivi", {
            'fields': ('cree_le', 'modifie_le'),
        }),
    )

    def has_module_permission(self, request):
        return True  # Permet d'afficher l'application dans l'admin

    def has_view_permission(self, request, obj=None):
        return True  # Permet de voir les objets

    def has_add_permission(self, request):
        return True  # Permet d'ajouter de nouveaux objets

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier les objets existants

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer les objets



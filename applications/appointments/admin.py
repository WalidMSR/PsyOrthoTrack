from django.contrib import admin
from .models import RendezVous

@admin.register(RendezVous)
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


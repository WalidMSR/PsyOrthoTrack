from django.contrib import admin
from .models import Evaluation
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect


# Register your models here.
# @admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom' , 'titre', 'date_de_creation_dossier', 'view_medical_records_button', 'export_medical_records_button')
    search_fields =  ('nom', 'prenom')



    
    def view_medical_records_button(self, obj):
        return format_html(
            '<a class="button" href="/evaluation/view_evaluation/{}"target="_blank" rel="noopener noreferrer">📁 Voir Dossiers</a>',
        obj.id
    )
    view_medical_records_button.short_description = ""

    def export_medical_records_button(self, obj):
        export_url = reverse('export_evaluation', args=[obj.id])  # Lien vers une vue pour exporter
        return format_html(
            '<a class="button" href="{}" style="color: white; background-color: green; padding: 5px 10px; border-radius: 5px; text-decoration: none;">📤 Exporter</a>',
            export_url
        )
    export_medical_records_button.short_description = " "

    def add_view(self, request, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('ajouter_eval'))
    
    
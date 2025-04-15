from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from applications.patients_docs.models import ProfilPatient
from django.utils.html import format_html
from django.urls import reverse
from django.forms import DateInput

admin_site = admin.AdminSite(name='admin_personnalise')

admin.site.site_header = "PsyOrthoTrack"

@admin.register(ProfilPatient)
class ProfilPatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_naissance', 'age' ,'genre',  'cree_le',"view_medical_records_button", "export_medical_records_button")
    list_filter = ('genre', 'cree_le')
    search_fields = ('prenom', 'nom', 'numero_telephone_1', 'numero_telephone_2')
    ordering = ('nom', 'prenom')
    verbose_name = "Documents et ressources "
    verbose_name_plural = "Documents et ressources "

    fieldsets = [
        ("Patients", {
            "fields": ['prenom', 'nom','date_naissance', 'lieu_naissance', 'genre','adresse',
                       'numero_telephone_1', 'numero_telephone_2', 'email', 'cree_le', 'photo'],
            "classes": ["tab"]
        }),
        
        ("Dossiers médicaux", {
            "fields": [
                "scolarite", "type_de_trouble", "demande", "envoye_par", "date_de_creation_dossier", "description", "prescription", "maladies_ou_handicaps_famille",
                "maladies_ou_handicaps_du_pere", "maladies_ou_handicaps_de_la_mere", "maladies_ou_handicaps_chez_les_freres", "lien_entre_les_parents", "nombre_freres_soeurs",
                "nombre_freres", "nombre_soeurs", "position_entre_les_freres", "sante_freres_soeurs", "antecedents_familiaux",
                "vie_parentale", "deces_mere", "deces_pere", "deces_parents", "enfant_vit_avec_les_parents",
                "composition_familiale", "profession_pere", "niveau_etudes_pere", "profession_mere", "niveau_etudes_mere",
                "niveau_economique", "temps_pour_soins_enfant", "grossesse_voulue", "grossesse_voulue_par_mere", "grossesse_voulue_par_pere",
                "sexe_voulu", "grossesse_compromise", "type_de_complication", "raison_grossesse_compromise", "maladies_mere",
                "prises_medicaments_mere", "accouchement_a_terme", "accouchement_avant_terme", "accouchement_apres_terme", "type_accouchement",
                "sejour_maternite", "etat_mere", "etat_enfant", "cri_de_naissance", "couleur_enfant",
                "poids_enfant", "mis_en_incubateur", "alimentation_enfant", "alimentation_enfant_duree", "sommeil_enfant",
                "antecedents_maladies_enfant", "maladies_enfance", "fievre", "jaunisse", "asthme",
                "aucune_maladie_enfance", "maladies_autres", "epilepsie", "meningite", "infections_oreilles",
                "hospitalisation", "age_hospitalisation", "developpement_psychomoteur", "marche", "chutes_frequentes",
                "sourire_visages_familier", "manger_seul", "sasseoir", "main", "controle_tete",
                "ramper", "acquisition_proprete", "s_habiller_seul", "audition", "vue",
                "langage", "babillage", "utilisation_phonemes", "utilisation_mots", "reponse_mots",
                "utilisation_phrase", "utilisation_jumelage", "langue_dans_maison", "langue_enfant_actuelle", "alimentation_et_deglutition",
                "type_alimentation", "position_alimentation", "voies_erronnees_alimentation", "mastication", "developpement_emotionnel",
                "relation_freres", "relation_avec_autres", "est_social", "aime_jouer_avec_autres", "enfants_avec_qui_il_joue",
                "comportement_a_la_maison", "sort_seul", "comportement_chez_lui", "etat_education_prescolaire", "retard_scolaire", "comportement_entretien",
                "autres_observations", "age_decouverte_maladie", "symptomes_apparents"
            ],
            "classes": ["tab"]
        }),
    ]

    formfield_overrides = {
        # Utilisez un widget avec un sélecteur d'année pour `date_naissance`
        ProfilPatient._meta.get_field('date_naissance'): {'widget': DateInput(attrs={'type': 'date'})},
    }

    def age(self, obj):
        return obj.age_calcule  # Appelle la propriété `age_calcule` du modèle
    age.short_description = "Âge"  # Définit le titre de la colonne dans l'admin

    def view_medical_records_button(self, obj):
        return format_html(
            '<a class="button" href="/patients_docs/view_medical_record/{}"target="_blank" rel="noopener noreferrer">📁 Voir Dossiers</a>',
            obj.id
        )
    view_medical_records_button.short_description = ""

    def export_medical_records_button(self, obj):
        export_url = reverse('export_medical_record', args=[obj.id])  # Lien vers une vue pour exporter
        return format_html(
            '<a class="button" href="{}" style="color: white; background-color: green; padding: 5px 10px; border-radius: 5px; text-decoration: none;">📤 Exporter</a>',
            export_url
        )
    export_medical_records_button.short_description = " "

# @admin.register("Medcin")
# class MedcinAdmin(admin.ModelAdmin):
#     list_display = ('nom', 'prenom')
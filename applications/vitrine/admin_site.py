from django.contrib import admin
from django import forms
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from applications.appointments.models import RendezVous
from applications.appointments.admin import RendezVousAdmin

from applications.evaluation.models import Evaluation
from applications.evaluation.admin import EvaluationAdmin

from applications.patients_docs.models import ProfilPatient
from applications.patients_docs.admin import ProfilPatientAdmin

from applications.vitrine.models import CustomUser, Cabinet
# from applications.vitrine.models import CustomUser, Cabinet, Paiement, Offre
# 👇 Personnalisation du CustomUserAdmin
class CustomUserCreationForm(UserCreationForm):
    is_active = forms.BooleanField(required=False, initial=True, label="Actif")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'nom_medecin', 'prenom_medecin', 'role', 'cabinet', 'is_active')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'nom_medecin', 'prenom_medecin', 'email', 'role', 'is_active')
    list_editable = ('is_active',)  # Cette ligne rend le champ "is_active" modifiable directement dans le tableau
    list_filter = ('role', 'is_active', 'cabinet')

    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnelles', {
            'fields': ('nom_medecin', 'prenom_medecin', 'age', 'sexe', 'telephone_perso', 'cabinet', 'role')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'nom_medecin', 'prenom_medecin', 'role', 'cabinet', 'is_active'),
        }),
    )

    search_fields = ('username', 'email', 'nom_medecin', 'prenom_medecin')
    ordering = ('username',)


# Interface Cabinet Admin

class CustomUserInline(admin.TabularInline):  # ou StackedInline
    model = CustomUser
    extra = 1
    fields = ('username', 'email', 'nom_medecin', 'prenom_medecin', 'telephone_perso', 'role', 'is_active')
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('name', 'ville', 'telephone', 'mail', 'medecin_nom', 'medecin_prenom', 'medecin_telephone', 'created_at')
    inlines = [CustomUserInline]
    search_fields = ('name', 'ville', 'mail')
    list_filter = ('ville',)

    def get_medecin(self, obj):
        # Tu peux adapter ce filtre selon le rôle exact des médecins
        return obj.customuser_set.filter(role='client').first()

    def medecin_nom(self, obj):
        medecin = self.get_medecin(obj)
        return medecin.nom_medecin if medecin else "—"
    medecin_nom.short_description = "Nom Médecin"

    def medecin_prenom(self, obj):
        medecin = self.get_medecin(obj)
        return medecin.prenom_medecin if medecin else "—"
    medecin_prenom.short_description = "Prénom Médecin"

    def medecin_telephone(self, obj):
        medecin = self.get_medecin(obj)
        return medecin.telephone_perso if medecin else "—"
    medecin_telephone.short_description = "Téléphone Médecin"





# class PaiementAdmin(admin.ModelAdmin):
#     list_display = ('user', 'offre', 'montant', 'date_paiement', 'status_paiement', 'cabinet', 'reference_bancaire', 'preuve_paiement')
#     list_filter = ('status_paiement',)
#     search_fields = ('user__username', 'offre__nom_offre', 'reference_bancaire')
    
#     # Ajouter une action personnalisée pour valider un paiement
#     actions = ['valider_paiement', 'activer_compte']

#     def valider_paiement(self, request, queryset):
#         queryset.update(status_paiement='paye')  # Modifie le statut du paiement à "Payé"
#         for paiement in queryset:
#             # Optionnel: Envoyer un e-mail de confirmation de paiement (vous pouvez personnaliser cela)
#             send_mail(
#                 'Confirmation de paiement',
#                 f'Votre paiement pour {paiement.offre.nom_offre} a été validé.',
#                 'support@votresite.com',
#                 [paiement.user.email]
#             )
#         self.message_user(request, "Les paiements ont été validés.")

#     def activer_compte(self, request, queryset):
#         """Cette fonction va activer le compte utilisateur après validation du paiement"""
#         for paiement in queryset:
#             if paiement.status_paiement == 'paye':
#                 # Active le compte utilisateur lié au paiement
#                 paiement.user.is_active = True
#                 paiement.user.save()
#                 self.message_user(request, f"Le compte de {paiement.user.username} a été activé.")

#     valider_paiement.short_description = "Valider le paiement"
#     activer_compte.short_description = "Activer le compte utilisateur"

# class OfferAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')
#     search_fields = ('name',)



# admin.site.register(Paiement, PaiementAdmin)
# admin.site.register(Offre, OfferAdmin)



class CabinetAdminSite(AdminSite):
    site_header = "Cabinet Admin"
    site_title = "Espace Client"
    index_title = "Dashboard Directeur de Cabinet"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_authenticated and request.user.role == 'client'


cabinet_admin_site = CabinetAdminSite(name='cabinetadmin')

# Enregistre les modèles nécessaires dans le cabinet_admin_site
cabinet_admin_site.register(CustomUser, CustomUserAdmin)
cabinet_admin_site.register(RendezVous, RendezVousAdmin)
cabinet_admin_site.register(Evaluation, EvaluationAdmin)
cabinet_admin_site.register(ProfilPatient, ProfilPatientAdmin)
cabinet_admin_site.register(Cabinet, CabinetAdmin) 
print("📋 Modèles enregistrés dans cabinet_admin_site :", list(cabinet_admin_site._registry.keys()))



# Interface SuperAdmin
class SuperAdminSite(AdminSite):
    site_header = "Administration principale"
    site_title = "Super Admin"
    index_title = "Dashboard Super Admin"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_authenticated and request.user.role == 'admin'


super_admin_site = SuperAdminSite(name='superadmin')
super_admin_site.register(CustomUser, CustomUserAdmin)  
super_admin_site.register(Cabinet, CabinetAdmin)
super_admin_site.register(RendezVous, RendezVousAdmin)
super_admin_site.register(Evaluation, EvaluationAdmin)
super_admin_site.register(ProfilPatient, ProfilPatientAdmin)




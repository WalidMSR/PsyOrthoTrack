from django.contrib import admin
# from .models import Cabinet, Medecin

# class CabinetAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'created_at')

#     # Cette méthode est utilisée pour filtrer l'accès en fonction du rôle de l'utilisateur
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
        
#         if request.user.is_superuser:  # Si c'est un superadmin, il peut voir tous les cabinets
#             return qs
        
#         # Si l'utilisateur est un médecin ou un membre du staff, on lui permet de voir son propre cabinet
#         try:
#             medecin = Medecin.objects.get(user=request.user)
#             return qs.filter(id=medecin.cabinet.id)  # Filtre pour ne montrer que son propre cabinet
#         except Medecin.DoesNotExist:
#             return qs.none()  # Si l'utilisateur n'est pas médecin, il ne peut pas voir les cabinets

# admin.site.register(Cabinet, CabinetAdmin)
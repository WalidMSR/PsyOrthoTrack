from django.contrib import admin


# Admin pour les super utilisateurs/admin principaux
class AdminCabinetModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Tout afficher pour le super admin
        qs = super().get_queryset(request)
        return qs

    def has_module_permission(self, request):
        # Super user/admin principal a accès à tous les modules
        return True

    def has_view_permission(self, request, obj=None):
        # Super user/admin principal peut voir tous les objets
        return True


class CabinetModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'medecin':
            return qs.filter(medecin=request.user)
        elif request.user.role == 'staff':
            return qs.filter(medecin__staff__in=[request.user])
        return qs.none()

    def has_module_permission(self, request):
        return request.user.role != 'admin'

    def has_view_permission(self, request, obj=None):
        return request.user.role != 'admin'

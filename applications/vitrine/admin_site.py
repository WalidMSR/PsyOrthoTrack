from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

User = get_user_model()

class SuperAdminSite(AdminSite):
    site_header = "Administration principale"
    site_title = "Super Admin"
    index_title = "Dashboard Super Admin"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_authenticated and request.user.role == 'admin'


class CabinetAdminSite(AdminSite):
    site_header = "Cabinet Admin"
    site_title = "Espace Client"
    index_title = "Dashboard Directeur de Cabinet"

    def has_permission(self, request):
        print("has_permission called with user:", request.user)
        return request.user.is_active and request.user.is_authenticated and request.user.role == 'client'

from django.contrib import admin
from .models import CustomUser, Cabinet

super_admin_site = SuperAdminSite(name='superadmin')
cabinet_admin_site = CabinetAdminSite(name='cabinetadmin')

# Enregistrement dans chaque interface selon le besoin
super_admin_site.register(CustomUser)
super_admin_site.register(Cabinet)

cabinet_admin_site.register(CustomUser)
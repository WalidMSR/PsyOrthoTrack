from django.urls import path
from . import views
from .admin_site import super_admin_site, cabinet_admin_site

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('no-admin-access/', views.no_admin_access, name='no_admin_access'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('connexion/', views.connexion, name = 'connexion'), 
    # path('cabinet-staff/', views.cabinet_staff_dashboard, name='cabinet_staff_dashboard'),
    path('admine/', super_admin_site.urls),
    path('cabinet-admin/', cabinet_admin_site.urls),

]
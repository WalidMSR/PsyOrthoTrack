from django.urls import path
from . import views
from .admin_site import super_admin_site, cabinet_admin_site
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.client_signup_view, name='login'),
    
    path('no-admin-access/', views.no_admin_access, name='no_admin_access'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.connexion, name = 'connexion'), 
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('validate-user/<int:user_id>/', views.validate_user, name='validate_user'),

    
    # path('cabinet-staff/', views.cabinet_staff_dashboard, name='cabinet_staff_dashboard'),
    path('user-admin/', super_admin_site.urls),
    path('cabinet-admin/', cabinet_admin_site.urls),

]
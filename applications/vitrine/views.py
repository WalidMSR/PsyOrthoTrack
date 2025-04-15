from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('/admin/')
            else:
                return redirect('no_admin_access')  # redirige vers une page personnalisée
        else:
            return redirect('no_admin_access')  # redirige vers une page personnalisée apres nzidha

    return render(request, 'login.html')


# @login_required
# def post_login_redirect(request):
#     if request.user.role == 'admin':
#         return redirect('/admin/')
#     elif request.user.role == 'medecin':
#         return redirect('/cabinet-admin/')  # tableau pour médecins
#     elif request.user.role == 'staff':
#         return redirect('/cabinet-staff/')  # tableau pour staff (plus restreint)
#     else:
#         return redirect('no_admin_access')
    
    


#une redirection vers une page personnalisée si l’utilisateur n’a pas accès à l’admin
def no_admin_access(request):
    return render(request, 'no_admin_access.html')

def logout_view(request):
    logout(request)
    return redirect('login')



def home(request):
    return render(request, 'home.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('home')
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
            return redirect('login')

    return render(request, 'connexion.html')


def cabinet_staff_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'staff':
        return redirect('no_admin_access')
    return render(request, 'cabinet/staff_dashboard.html')  # à toi de le créer

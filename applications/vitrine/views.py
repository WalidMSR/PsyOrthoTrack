from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# from .models import Paiement

from applications.vitrine.forms import  ConnexionForm ,ClientSignupForm


# from .forms import ClientSignupForm


def no_admin_access(request):
    return render(request, 'no_admin_access.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            identifiant = form.cleaned_data['identifiant']
            password = form.cleaned_data['password']

            # Vérifie si l'identifiant est une adresse email
            if '@' in identifiant:
                try:
                    user_obj = User.objects.get(email=identifiant)
                    username = user_obj.username
                except User.DoesNotExist:
                    username = None
            else:
                username = identifiant

            if username:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Connexion réussie.')
                    if user.is_superuser:
                        return redirect('/user-admin/')
                    elif hasattr(user, 'role') and user.role == 'client':
                        return redirect('/cabinet-admin/')
                    else:
                        return redirect('/connexion/')
                else:
                    messages.error(request, 'Nom d\'utilisateur ou Mot de passe incorrect.')
            else:
                messages.error(request, 'Utilisateur non trouvé.')
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', {'form': form})


def cabinet_staff_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'staff':
        return redirect('no_admin_access')
    return render(request, 'cabinet/staff_dashboard.html')  # à toi de le créer




def validate_user(request, user_id):
    # Récupérer l'utilisateur
    user = get_user_model().objects.get(id=user_id)

    # Vérification des paiements et des offres associées
    paiement = Paiement.objects.filter(user=user, status_paiement='paye').first()
    if paiement:
        # Si le paiement est validé, activer l'utilisateur
        user.is_active = True
        user.save()

        # Envoi de l'email de confirmation
        send_mail(
            'Compte activé',
            f"Bonjour {user.username},\n\nVotre compte a été activé. Voici un résumé de votre inscription :\n\nNom d'utilisateur : {user.username}\nEmail : {user.email}\nOffre choisie : {paiement.offre.nom_offre}\nMontant payé : {paiement.montant} Dz\nDate d'inscription : {user.date_joined.strftime('%Y-%m-%d')}\nDate de validation : {now().strftime('%Y-%m-%d')}\n\nMerci de votre confiance.",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        # Rediriger vers une page de confirmation ou vers l'accueil
        return redirect('home')  # Ou une autre page de votre choix
    else:
        # Si le paiement n'est pas trouvé ou non validé
        return redirect('error')
    
def client_signup_view(request):
    if request.method == 'POST':
        form = ClientSignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Envoi d'email à l'admin
            admin_msg = f"""
                            Nouvelle demande d'inscription :

                            \tNom d'utilisateur : {user.username}
                            \tNom médecin : {user.nom_medecin}
                            \tPrénom : {user.prenom_medecin}
                            \tTéléphone : {user.telephone_perso}
                            \tEmail : {user.email}
                            \tNom Cabinet : {user.cabinet.name}
                            \tAdresse : {user.cabinet.address}
                            \tVille : {user.cabinet.ville}
                        """
            send_mail(
                subject="Nouvelle inscription cabinet",
                message=admin_msg,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # Email au client
            send_mail(
                subject="Inscription en attente de validation",
                message="Merci pour votre inscription. Nous allons vérifier votre paiement et activer votre compte sous peu.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return render(request, 'inscription_success.html')
    else:
        form = ClientSignupForm()
    return render(request, 'login.html', {'form': form})


# def payment_view(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST, request.FILES)
#         if form.is_valid():
#             payment = form.save()

#             # Optionnel: envoyer un e-mail de confirmation à l'utilisateur
#             send_mail(
#                 'Confirmation de votre paiement',
#                 f'Votre paiement a été effectué avec succès. Montant payé: {payment.amount_paid}€.',
#                 'support@votresite.com',
#                 [payment.user.email]
#             )

#             return redirect('payment_success')
#     else:
#         form = PaymentForm()

#     return render(request, 'payment_page.html', {'form': form})
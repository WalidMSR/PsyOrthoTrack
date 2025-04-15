from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Cabinet, Offre
from django.core.validators import FileExtensionValidator

# from vitrine.models import CustomUser, Paiement

class ConnexionForm(forms.Form):
    identifiant = forms.CharField(
        label='Email ou nom d’utilisateur',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email ou nom d’utilisateur',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Mot de passe',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )


# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Paiement
#         fields = ['user', 'offer', 'transaction_id', 'amount_paid', 'proof_url']

#     def clean(self):
#         cleaned_data = super().clean()
#         amount_paid = cleaned_data.get('amount_paid')
#         offer = cleaned_data.get('offer')

#         if amount_paid != offer.price:
#             raise forms.ValidationError("Le montant payé ne correspond pas au prix de l'offre.")
#         return cleaned_data


class ClientSignupForm(UserCreationForm):
    # Champs pour les informations du cabinet
    cabinet_name = forms.CharField(
        label="Nom du Cabinet",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )
    cabinet_address = forms.CharField(
        label="Adresse du Cabinet",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )
    cabinet_ville = forms.CharField(
        label="Ville",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )
    cabinet_telephone = forms.CharField(
        label="Téléphone",
        required=False,
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )
    cabinet_mail = forms.EmailField(
        label="Email du Cabinet",
        required=False,
        widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )

    # # Nouveau champ pour choisir l'offre de paiement
    # offre_paiement = forms.ModelChoiceField(
    #     queryset=Offre.objects.all(),
    #     label="Choisir une Offre de Paiement",
    #     widget=forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    # )

    # # Nouveau champ pour la preuve de paiement (fichier)
    # preuve_paiement = forms.FileField(
    #     label="Télécharger la Preuve de Paiement",
    #     required=False,
    #     widget=forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
    #     validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'pdf', 'jpeg'])]
    # )

    class Meta:
        model = CustomUser
        
        fields = ['username', 'email', 'nom_medecin', 'prenom_medecin', 'age', 'sexe', 'telephone_perso']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'nom_medecin': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'prenom_medecin': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'age': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'sexe': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'telephone_perso': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'client'
        user.is_active = False  # L'utilisateur sera activé manuellement après validation
        if commit:
            # Créer d'abord l'instance de Cabinet
            cabinet = Cabinet.objects.create(
                name=self.cleaned_data['cabinet_name'],
                address=self.cleaned_data['cabinet_address'],
                ville=self.cleaned_data['cabinet_ville'],
                telephone=self.cleaned_data['cabinet_telephone'],
                mail=self.cleaned_data['cabinet_mail']
            )
            user.cabinet = cabinet
            # Sauvegarder l'utilisateur pour obtenir une PK
            user.save()
            
            # Créer ensuite l'instance de Paiement liée à l'utilisateur et au cabinet
            # paiement = Paiement.objects.create(
            #     user=user,
            #     cabinet=cabinet,
            #     offre=self.cleaned_data['offre_paiement'],
            #     preuve_paiement=self.cleaned_data.get('preuve_paiement', None),
            #     status_paiement='en_attente'
            # )
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # On applique manuellement les attributs Tailwind sur password1 et password2
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg',
            # 'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg',
            # 'placeholder': 'Confirmez le mot de passe'
        })

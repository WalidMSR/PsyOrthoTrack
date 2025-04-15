from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator



class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Offre(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name='offres')
    nom_offre = models.CharField(max_length=100)  # Exemple : "Forfait de base", "Consultation spécialisée"
    description = models.TextField()  # Description de ce que comprend l'offre
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # Tarif de l'offre

    def __str__(self):
        return f"{self.nom_offre} - {self.prix} Dz"
    



# class Paiement(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='paiements')
#     cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name='paiements')
#     offre = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name='paiements')  # L'offre choisie
#     montant = models.DecimalField(max_digits=10, decimal_places=2)
#     date_paiement = models.DateField(null=True, blank=True)
#     status_paiement = models.CharField(
#         max_length=20,
#         choices=[
#             ('en_attente', 'En attente'),
#             ('paye', 'Payé'),
#             ('echoue', 'Échoué'),
#         ],
#         default='en_attente',
#     )
#     reference_bancaire = models.CharField(max_length=100, blank=True, null=True)  # Numéro de référence bancaire
#     preuve_paiement = models.FileField(
#         upload_to='paiements/preuves/',
#         blank=True,
#         null=True,
#         validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'pdf', 'jpeg'])]
#     )
#     description = models.TextField(blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.montant:
#             self.montant = self.offre.prix  # Applique le prix de l'offre
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Paiement de {self.user.username} pour {self.offre.nom_offre} à {self.cabinet.name} - {self.montant} Dz"
        

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin Principal'),
        ('client', 'Directeur de Cabinet'),
        ('staff', 'Staff'),
    ]
    nom_medecin = models.CharField(max_length=100, null=True, blank=True)
    prenom_medecin = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    sexe = models.CharField(max_length=10, choices=[('Homme', 'Homme'), ('Femme', 'Femme')], null=True, blank=True)
    telephone_perso = models.CharField(max_length=15, null=True, blank=True)
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.SET_NULL, null=True, blank=True)

    # is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"
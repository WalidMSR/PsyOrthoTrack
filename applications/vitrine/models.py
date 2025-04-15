from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('medecin', 'Médecin'),
#         ('staff', 'Staff'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='medecin')

#     # Si tu veux que le staff soit lié à un cabinet (utilisateur médecin)
#     cabinet = models.ForeignKey(
#         'self',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         limit_choices_to={'role': 'medecin'},
#         related_name='staff_users'
#     )

# class Cabinet(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class Medecin(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cabinet = models.ForeignKey(Cabinet, related_name='medecins', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin Principal'),
        ('client', 'Directeur de Cabinet'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
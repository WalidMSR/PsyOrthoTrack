from django.db import models
from django.utils import timezone

class Evaluation(models.Model):
    prenom = models.CharField(max_length=255, blank=True, null=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_de_creation_dossier = models.DateField("Date du dossier",default=timezone.now, blank=True, null=True)
    score1 = models.IntegerField(blank=True, null=True)
    score2 = models.IntegerField(blank=True, null=True)
    score3 = models.IntegerField(blank=True, null=True)
    score4 = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('nom', 'prenom')  # Empêche les doublons exacts
        ordering = ['nom', 'prenom']
        verbose_name = "Evaluations"
        verbose_name_plural = "Evaluations"
    
    
    def __str__(self):
        return self.titre



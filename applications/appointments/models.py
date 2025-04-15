from django.db import models
from datetime import timedelta
from django.utils import timezone
class RendezVous(models.Model):
    STATUT_CHOICES = [
        ('prévu', 'Prévu'),
        ('terminé', 'Terminé'),
        ('annulé', 'Annulé'),
        ('reporté', 'Reporté'),
    ]

    TYPE_SEANCE_CHOICES = [
        ('évaluation', 'Évaluation'),
        ('rééducation', 'Rééducation'),
        ('suivi', 'Suivi'),
        ('consultation', 'Consultation'),
    ]

    patient = models.ForeignKey('patients_docs.ProfilPatient', on_delete=models.CASCADE, null=True)
    nom_patient = models.CharField("Nom du patient", max_length=100, blank=True, null=True)
    date = models.DateField("Date")
    heure = models.TimeField("Heure")
    
    duree = models.DurationField("Durée prévue", default=timedelta(minutes=30))
    statut = models.CharField("Statut", max_length=10, choices=STATUT_CHOICES, default='prévu')
    type_seance = models.CharField("Type de séance", max_length=20, choices=TYPE_SEANCE_CHOICES, null=True)
    description = models.TextField("Notes / Description", blank=True, null=True)

    telephone = models.CharField("Téléphone du patient", max_length=20, blank=True, null=True)
    email = models.EmailField("Email du patient", blank=True, null=True)

    teleconsultation = models.BooleanField("Téléconsultation ?", default=False)

    prix = models.DecimalField("Prix (€)", max_digits=6, decimal_places=2, null=True, blank=True)
    est_paye = models.BooleanField("Payé ?", default=False)

    cree_le = models.DateTimeField("Créé le", default=timezone.now, blank=True, null=True)  # Créé le
    modifie_le = models.DateTimeField("Modifié le", auto_now=True)

    def str(self):
        return f"{self.nom_patient} - {self.date} à {self.heure} ({self.type_seance})"
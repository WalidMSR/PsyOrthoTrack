from django.db import models

# Create your models here.
class rendezvous(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    patient = models.CharField(max_length=100)
    docteur = models.CharField(max_length=100)
    motif = models.TextField()
    status = models.CharField(max_length=20, default='en attente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"
        ordering = ['date', 'heure']
    def __str__(self):  
        return f"Rendez-vous de {self.patient} avec {self.docteur} le {self.date} à {self.heure}"
    def save(self, *args, **kwargs):
        # Vérifier si le rendez-vous existe déjà
        if rendezvous.objects.filter(date=self.date, heure=self.heure, patient=self.patient).exists():
            raise ValueError("Un rendez-vous existe déjà à cette date et heure pour ce patient.")
        super().save(*args, **kwargs)
    def get_status_display(self):
        return self.status
    def get_patient_display(self):
        return self.patient
    def get_docteur_display(self):
        return self.docteur
    def get_motif_display(self):
        return self.motif
    def get_created_at_display(self):
        return self.created_at
    def get_updated_at_display(self):
        return self.updated_at
    def get_date_display(self):
        return self.date    
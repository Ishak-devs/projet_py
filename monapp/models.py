from django.db import models

# Create your models here.

class Calendrier(models.Model):
    jour = models.CharField(max_length=100)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.jour} : {self.heure_debut} - {self.heure_fin}"
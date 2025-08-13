from django.db import models

# Create your models here.

class Evenements(models.Model):
    Titre = models.CharField(max_length=100)
    jour = models.CharField(max_length=100)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    infos_complementaires = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.jour} : {self.heure_debut} - {self.heure_fin}"
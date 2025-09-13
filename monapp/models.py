from django.db import models
from datetime import datetime

# Create your models here.

class Evenements(models.Model):
    Titre = models.CharField(max_length=100)
    organisateur_nom = models.CharField(max_length=150 , default="Inconnu")
    lieu = models.CharField(max_length=150 , default="En ligne")
    date = models.DateField(default=datetime.now)



    def __str__(self):
        return f"{self.Titre} : {self.organisateur_nom}"


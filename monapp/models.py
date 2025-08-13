from django.db import models

# Create your models here.

class Evenements(models.Model):
    Titre = models.CharField(max_length=100)
    organisateur_nom = models.CharField(max_length=150 , default="inconnu")

    def __str__(self):
        return f"{self.Titre} : {self.organisateur_nom}"
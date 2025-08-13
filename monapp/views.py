from django.contrib.messages.api import success
from django.http import HttpResponse
from django.shortcuts import render
from .models import Evenements
from rich.console import Console

console = Console()

# Create your views here.
def accueil(request):
    return render(request, "index.html")

def Ajout_event(request):
    if request.method == 'POST':
            Titre = request.POST.get('Titre')
            organisateur_nom = request.POST.get('organisateur_nom')

            if Titre and organisateur_nom:
                Evenements.objects.create(Titre=Titre, organisateur_nom=organisateur_nom)
                console.print('données ajoutés')

            return render(request, 'index.html')
    return None

def afficher_event (request):
   evenements = Evenements.objects.all()
   return render(request, 'index.html', {'evenements': evenements})

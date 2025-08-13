from django.contrib.messages.api import success
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Evenements
from rich.console import Console

console = Console()

# Create your views here.
def accueil(request):

    evenements = Evenements.objects.all()
    return render(request, 'index.html', {'evenements': evenements})


def Ajout_event(request):
    if request.method == 'POST':
            Titre = request.POST.get('Titre')
            organisateur_nom = request.POST.get('organisateur_nom')

            if Titre and organisateur_nom:
                Evenements.objects.create(Titre=Titre, organisateur_nom=organisateur_nom)
                console.print('données ajoutés')

            return redirect('accueil')
    return render(request, 'index.html')

def supprimer_event(request):
    if request.method == 'POST':
        Titre = request.POST.get('Titre')
        organisateur = request.POST.get('organisateur_nom')

        Evenements.objects.filter(Titre=Titre, organisateur_nom=organisateur)

        return redirect('accueil')
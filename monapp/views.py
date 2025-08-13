from django.http import HttpResponse
from django.shortcuts import render
from models import Evenements

# Create your views here.
def accueil(request):
    return render(request, "index.html")

def Ajout_event(request):
    if request.method == 'POST':
            Titre = request.POST.get('Titre')
            oroganisateur_nom = request.POST.get('organisateur_nom')

            Evenements.objects.create(Titre=Titre, oroganisateur_nom= oroganisateur_nom)

            return render(request, 'index.html')
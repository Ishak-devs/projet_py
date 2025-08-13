from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, "index.html")

def Ajout_event():


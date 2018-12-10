from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import *

def index(request):
    context = {
        'form': PlantSpeciesForm(),
    }
    return render(request, 'plants/home.html', context)
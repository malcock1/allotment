from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import PlantSpecies
from .forms import *

def index(request):
    context = {
        'form': PlantSpeciesForm(),
        'plants': PlantSpecies.objects.all(),
    }
    if request.method == "POST":
    	form = PlantSpeciesForm(request.POST)
    	if form.is_valid():
    		new_plant = form.save()

    return render(request, 'plants/home.html', context)
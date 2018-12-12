from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import PlantSpecies
from .forms import *

def dashboard(request):
	"""
	This wants moving
	"""
	context = {
		'page_title': "Dashboard",
	}

	return render(request, 'allotment/base.html', context)

def plants_home(request):
	context = {
		'page_title': 'Plants home',
		'form': PlantSpeciesForm(),
		'species': PlantSpecies.objects.all(),
	}
	if request.method == "POST":
		form = PlantSpeciesForm(request.POST)
		if form.is_valid():
			new_plant = form.save()

	return render(request, 'plants/home.html', context)


def plant_species_view(request, species_id):
	species = PlantSpecies.objects.get(pk=species_id)
	context = {
		'page_title': "Species: {}".format(species),
		'species': species,
	}
	return render(request, 'plants/species_view.html', context)


def plant_species_add(request):
	context = {
		'page_title': 'Add a plant species',
		'form': PlantSpeciesForm(),
	}
	if request.method == "POST":
		form = PlantSpeciesForm(request.POST)
		if form.is_valid():
			new_plant = form.save()
		else:
			context['form'] = form
	return render(request, 'plants/species_form.html', context)

	
def plant_species_edit(request, species_id):
	species = PlantSpecies.objects.get(pk=species_id)
	context = {
		'page_title': 'Edit {}'.format(species),
		'form': PlantSpeciesForm(instance=species),
	}
	if request.method == "POST":
		form = PlantSpeciesForm(request.POST, instance=species)
		if form.is_valid():
			plant = form.save()
		else:
			context['form'] = form
	return render(request, 'plants/species_form.html', context)
	

def plant_species_delete(request, species_id):
	species = PlantSpecies.objects.get(pk=species_id)
	name = species.name
	species.delete()
	messages.add_message(request, messages.INFO, '{} deleted'.format(name))
	return redirect('plants_home')


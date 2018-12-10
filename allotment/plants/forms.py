from django import forms
from django.forms import ModelForm

from .models import PlantSpecies, \
					Plant

class PlantSpeciesForm(ModelForm):
	class Meta:
		model = PlantSpecies
		exclude = ('companions',)

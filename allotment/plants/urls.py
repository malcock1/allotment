from django.conf.urls import url
import plants
from .views import *

urlpatterns = [
    url(r'^$', plants_home, name='plants_home'),
    url(r'^species/(?P<species_id>[0-9]+)/$', plant_species_view, name='plant_species_view'),
    url(r'^species/add/$', plant_species_add, name='plant_species_add'),
    url(r'^species/edit/(?P<species_id>[0-9]+)/$', plant_species_edit, name='plant_species_edit'),
    url(r'^species/delete/(?P<species_id>[0-9]+)/$', plant_species_delete, name='plant_species_delete'),
]
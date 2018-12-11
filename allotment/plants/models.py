from django.db import models

LIGHT_CHOICES = [
	(1,'Full shade'),
	(2,'Partial shade'),
	(3,'Shade tolerant'),
	(4,'Partial sun'),
	(5,'Full sun'),
]

class PlantSpecies(models.Model):
	name = models.CharField(max_length=128)
	latin_name = models.CharField(max_length=128, null=True, blank=True)

	seed_indoors = models.ManyToManyField("planner.Month", related_name='plants_to_seed_indoors')
	seed_outdoors = models.ManyToManyField("planner.Month", related_name='plants_to_seed_outdoors')
	plant_out = models.ManyToManyField("planner.Month", related_name='plants_to_plant_out')
	harvest = models.ManyToManyField("planner.Month", related_name='plants_to_harvest')

	full_height = models.PositiveSmallIntegerField(null=True, blank=True) # In centimeters
	full_diameter = models.PositiveSmallIntegerField(null=True, blank=True) # In centimeters
	light = models.PositiveSmallIntegerField(choices=LIGHT_CHOICES, null=True, blank=True)
	water = models.PositiveSmallIntegerField(null=True, blank=True) # How much it needs from 1-5

	notes = models.TextField(null=True, blank=True)

	annual = models.BooleanField(default=False)

	companions = models.ManyToManyField("self", related_name='companions') # Species that go well together

	def __str__(self):
		if self.latin_name:
			return "{} ({})".format(self.name, self.latin_name)
		else:
			return self.name


class Bed(models.Model):
	"""
	Location in the allotment 
	We might have to do something like the tile system on plantz...
	This is very very unfinished :P
	"""
	x = models.PositiveSmallIntegerField(null=True)
	y = models.PositiveSmallIntegerField(null=True)
	

class PlantSource(models.Model):
	name = models.CharField(max_length=128)
	web_address = models.CharField(max_length=256)


class Plant(models.Model):
	""" An instance of a real physical plant or seed """
	species = models.ForeignKey(PlantSpecies, on_delete=models.PROTECT)
	location = models.ForeignKey(Bed, null=True, on_delete=models.SET_NULL)
	# Could put harvested weight in here?
	source = models.ForeignKey(PlantSource, null=True, on_delete=models.SET_NULL)
	cost = models.PositiveSmallIntegerField() # In pence per plant/seed


class Harvest(models.Model):
	"""
	When we harvest we can store some info about the plants,
	quantities, comments etc
	"""
	plants = models.ManyToManyField(Plant)
	# Not sure about this bit, probably put it in too soon
	# Consider having M2M field for beds, plant species
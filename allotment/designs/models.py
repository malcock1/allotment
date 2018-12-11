from django.db import models
from plants.models import Plant

# Create your models here.
class Design(models.Model):
    """
    This model defines a design layout for the allotment

    The width and height properties will be used to calculate
    the DIV grid in the template. A size of 1 will equal 1 metre
    but a grid will split a metre into multiple DIVS(not sure how
    many yet!)

    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    width = models.IntegerField()
    height = models.IntegerField()

    def __unicode__(self):
        return "Design: " + self.name

class Bed(models.Model):
    """
    This model is a raise bed or an area to plant plants
    it has a ForeignKey to th associated design.
    """

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    width = models.IntegerField()
    height = models.IntegerField()
    design = models.ForeignKey(Design, on_delete=models.SET_NULL, null=True)
    plants = models.ManyToManyField(Plant, blank=True, null=True)  # From plants.models.Plant

    def __unicode__(self):
        return "Bed: " + self.name



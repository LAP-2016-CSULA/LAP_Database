"""
Definition of models.
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class SpeciesType(models.Model):
    """
    Types of species used in the project e.g. birds, trees, etc.
    """
    species_name = models.CharField(max_length=45)

    def __str__(self):
        return self.species_name

@python_2_unicode_compatible
class Species(models.Model):
    """
    Exact organism in a species group e.g. a great dane (type of dog)
    """
    species_type_id = models.ForeignKey(SpeciesType, on_delete=models.CASCADE) 
    common_name = models.CharField(max_length=45)
    scientific_name = models.CharField(max_length=255)

    def __str__(self):
        return self.common_name
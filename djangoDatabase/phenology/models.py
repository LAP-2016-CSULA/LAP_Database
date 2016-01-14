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
    species_type = models.ForeignKey(SpeciesType, on_delete=models.CASCADE) 
    common_name = models.CharField(max_length=45, help_text="Enter the common known name of the species e.g. human")
    scientific_name = models.CharField(max_length=255, help_text="Enter the scientific name of a species e.g. homo sapiens")
    general_info = models.CharField(max_length=4096, default="",  help_text="Enter general information about the species")

    def __str__(self):
        return self.common_name

@python_2_unicode_compatible
class SpecificSpeciesQuestion(models.Model):
    """
    Questions concerning the phenological information of a specific species
    """
    subject_species = models.ForeignKey(Species, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, help_text="But a question about a species here")

    def __str__(self):
        readable_string = self.subject_species, self.question
        return readable_string

@python_2_unicode_compatible 
class SpeciesAnswer(models.Model):
    """
    The answer relate to a question - currently only offers boolean answers
    """
    question = models.ForeignKey(SpecificSpeciesQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, default="True or False?")
    answer_boolean = models.BooleanField(default=False)

    #Below string may change if/when we offer more answer types
    def __str__(self):
        return str(self.answer)
    
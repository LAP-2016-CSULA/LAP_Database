from django.contrib import admin
from phenology.models import SpeciesType, Species, SpeciesAnswer, SpecificSpeciesQuestion

admin.site.register(SpeciesType)
admin.site.register(Species)
admin.site.register(SpecificSpeciesQuestion)
admin.site.register(SpeciesAnswer)
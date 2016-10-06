from django.apps import AppConfig
from django.contrib import algoliasearch
from .index import LugaresIndex

class PlacesConfig(AppConfig):
    name = 'places'

    def ready(self):
        Lugares = self.get_model('Lugares')
        algoliasearch.register(Lugares, LugaresIndex)

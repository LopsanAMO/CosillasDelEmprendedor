from django.contrib.algoliasearch import AlgoliaIndex

class LugaresIndex(AlgoliaIndex):
    fields = ('nombre', 'descripcion')
    settings = {'attributesToIndex': fields}

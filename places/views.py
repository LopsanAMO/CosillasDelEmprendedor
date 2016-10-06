from django.shortcuts import render
from django.views.generic import TemplateView

class Prueba(TemplateView):
    template_name = 'api/prueba.html'

from django.db import models

class Lugares(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    latitud = models.CharField(blank=False, null=False, max_length=100)
    longitud = models.CharField(blank=False, null=False, max_length=100)
    lugares_cercanos = models.CharField(blank=False, null=False, max_length=100)
    historio_lugar = models.CharField(blank=False, null=False, max_length=100)
    horario = models.CharField(blank=False, null=False, max_length=100)
    costo_entrada = models.CharField(blank=False, null=False, max_length=100)

class Foto(models.Model):
    lugar = models.OneToOneField(Lugares, blank=False, null=False, related_name="fotos")
    foto = models.ImageField(blank=False, null=False)

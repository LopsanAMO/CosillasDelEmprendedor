from django.db import models

class Lugares(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    latitud = models.CharField(blank=False, null=False, max_length=100)
    longitud = models.CharField(blank=False, null=False, max_length=100)
    lugares_cercanos = models.CharField(blank=False, null=False, max_length=100)
    historio_lugar = models.CharField(blank=False, null=False, max_length=1000)
    horario = models.CharField(blank=False, null=False, max_length=100)
    costo_entrada = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return "{}".format(self.nombre)

class Foto(models.Model):
    lugar = models.ForeignKey(Lugares, blank=False, null=False, related_name="fotos")
    foto = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "Foto de lugar: {}".format(self.lugar)

class dangerzone(models.Model):
    nombre = models.CharField(blank=True, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return "zona de peligro: {}".format(self.nombre)

class dangerzonlatlng(models.Model):
    nombre = models.ForeignKey(dangerzone, blank=False, null=False, related_name="zonas")
    latitud = models.CharField(blank=False, null=False, max_length=100)
    longitud = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return "lat y lng de: {}".format(self.nombre)

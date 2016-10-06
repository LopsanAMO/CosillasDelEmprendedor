from django.contrib import admin
from .models import Lugares, Foto, dangerzone, dangerzonlatlng

@admin.register(Lugares)

class adminLugar(admin.ModelAdmin):
    list_display = ('nombre','latitud','longitud')

@admin.register(Foto)

class adminFoto(admin.ModelAdmin):
    list_display = ('lugar', 'foto')

@admin.register(dangerzone)

class adminDanger(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(dangerzonlatlng)

class adminDangerLatLong(admin.ModelAdmin):
    list_display = ('nombre', 'latitud', 'longitud')

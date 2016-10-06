from django.contrib import admin
from .models import Lugares, Foto

@admin.register(Lugares)

class adminLugar(admin.ModelAdmin):
    list_display = ('nombre','latitud','longitud')

@admin.register(Foto)

class adminFoto(admin.ModelAdmin):
    list_display = ('lugar', 'foto')    

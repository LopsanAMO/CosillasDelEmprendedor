from rest_framework import serializers
from ..models import Lugares, Foto, dangerzone, dangerzonlatlng

class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'

class LugaresSerializer(serializers.ModelSerializer):
    fotos = FotosSerializer(many=True)
    class Meta:
        model = Lugares
        fields = ('nombre','descripcion','latitud','longitud','lugares_cercanos','historio_lugar','horario','costo_entrada','fotos')
        deph = 1

class LatLngSerializer(serializers.ModelSerializer):
    class Meta:
        model = dangerzonlatlng
        fields = '__all__'

class DangerZoneSerializer(serializers.ModelSerializer):
    zonas = LatLngSerializer(many=True)
    class Meta:
        model = dangerzone
        fields = ('nombre','descripcion','zonas')
        deph = 1

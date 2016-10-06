from rest_framework import serializers
from ..models import Lugares, Foto

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

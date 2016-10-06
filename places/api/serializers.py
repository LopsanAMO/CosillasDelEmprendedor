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
        fields = ('')
        deph = 1

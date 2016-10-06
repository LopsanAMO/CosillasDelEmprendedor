from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..models import Lugares, Foto
from .serializers import FotosSerializer, LugaresSerializer
from utils.algoritmos import distance

@api_view(['GET', 'POST'])

def lugares_con_gps(request):
    if request.method == 'GET':
        # latitud = request.GET.get('lat')
        # longitud = request.GET.get('lon')
        lugar_gps_lat = -99.1209097
        lugar_gps_lon = 19.4133171
        #lugar_gps_obj = Lugares.objects.all().filter(longitud=lugar_gps_lon).filter(latitud=lugar_gps_lat)
        lugares = Lugares.objects.all()
        for i in range(len(lugares)):
            latitud2 = float(lugares.latitud)
            longitud2 = float(lugares.latitud)

            print('la wea intensificada')
        try:
            serializer = LugaresSerializer(lugares, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            print(type(e))
    else:
        print('oko')

@api_view(['GET', 'POST'])

def lugares_sin_gps(request):
    if request.method == 'GET':
        lugares = Lugares.objects.all()
        print('holaaaaaaaaaaaaaaaaaaaaaaaaa')
        try:
            serializer = LugaresSerializer(lugares, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            print(type(e))
    else:
        print('oko')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..models import Lugares, Foto
from .serializers import FotosSerializer, LugaresSerializer

# @api_view(['GET', 'POST'])
#
# def lugares_con_gps(request):
#     if request.method = 'POST':
#         latitud = request.GET.get('lat')
#         longitud = request.GET.get('lon')
#

@api_view(['GET', 'POST'])

def lugares_sin_gps(request):
    if request.method == 'GET':
        lugares = Lugares.objects.all()
        try:
            serializer = LugaresSerializer(lugares, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            print(type(e))
    else:
        print('oko')

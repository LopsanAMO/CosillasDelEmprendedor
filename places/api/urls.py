from django.conf.urls import url
from .views import lugares_sin_gps, lugares_con_gps, lugares_peligrosos
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^lugares/', csrf_exempt(lugares_sin_gps), name="lugares_api"),
    url(r'^lugaresgps/', csrf_exempt(lugares_con_gps), name='lugares_api_gps'),
    url(r'^peligroso/', csrf_exempt(lugares_peligrosos), name='lugares_peligrosos'),
]

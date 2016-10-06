from django.conf.urls import url
from .views import lugares_sin_gps
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^lugares', csrf_exempt(lugares_sin_gps), name="lugares_api")
]

from django.conf.urls import url, include
from django.contrib import admin
from places.api import urls as placesAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lugares/', include(placesAPI)),
]

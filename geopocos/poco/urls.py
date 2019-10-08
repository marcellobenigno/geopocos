from django.urls import path

from . import views as v

app_name = 'poco'

urlpatterns = [
    path('geojson/', v.PocoGeoJson.as_view(), name='poco_geojson'),
    path('pocos.js/', v.pocos_js, name='pocos_js'),
]

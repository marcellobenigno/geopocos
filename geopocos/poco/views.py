from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView

from geopocos.poco.models import Poco


class PocoGeoJson(GeoJSONLayerView):
    model = Poco
    properties = ('popup_content', 'q_m3h',)
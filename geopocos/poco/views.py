from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView

from geopocos.poco.models import Poco


class PocoGeoJson(GeoJSONLayerView):
    model = Poco
    properties = ('popup_content',)


def pocos_js(request):
    pocos = Poco.objects.all()
    context = {
        'object_list': pocos,
    }
    return render(request, 'poco/poco_js.html', context)

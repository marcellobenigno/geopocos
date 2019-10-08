from django.db.models import Max
from django.shortcuts import render

from geopocos.poco.models import Poco


def index(request):
    return render(request, 'core/index.html')


def mapa(request):
    q_max = Poco.objects.aggregate(Max('q_m3h'))

    context = {
        'q_max': q_max,
    }

    return render(request, 'core/mapa.html', context)

import os
from django.contrib.gis.utils import LayerMapping

from .models import Poco

poco_mapping = {
    'proprietario': 'proprietar',
    'orgao': 'orgao',
    'data_perfuracao': 'data_perfu',
    'profundidade': 'profundida',
    'q_m3h': 'q_m3h',
    'equipamento': 'equipament',
    'geom': 'POINT',
}

poco_shp = os.path.abspath(os.path.join('data', 'pocos.shp'))


def run(verbose=True):
    lm = LayerMapping(Poco, poco_shp, poco_mapping)
    lm.save(strict=True, verbose=verbose)
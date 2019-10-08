import os
from django.contrib.gis.utils import LayerMapping

from .models import Poco

poco_mapping = {
    'proprietario': 'PROPRIETAT',
    'orgao': 'ORGAO',
    'data_perfuracao': 'DATAPERFUR',
    'profundidade': 'PROFUNDIDA',
    'q_m3h': 'Q',
    'equipamento': 'EQUIPAMENT',
    'geom': 'POINT',
}

poco_shp = os.path.abspath(os.path.join('data', 'pocos.shp'))


def run(verbose=True):
    lm = LayerMapping(Poco, poco_shp, poco_mapping)
    lm.save(strict=True, verbose=verbose)
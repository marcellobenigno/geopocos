import os

from django.contrib.gis.utils import LayerMapping

from .models import Municipio

# Auto-generated `LayerMapping` dictionary for Municipio model
municipio_mapping = {
    'nome': 'nome',
    'cod_ibge_m': 'cod_ibge_m',
    'geom': 'MULTIPOLYGON',
}

municipio_shp = os.path.abspath(os.path.join('data', 'municipios_pb.shp'))


def run(verbose=True):
    lm = LayerMapping(Municipio, municipio_shp, municipio_mapping)
    lm.save(strict=True, verbose=verbose)

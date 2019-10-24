from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Municipio


@admin.register(Municipio)
class MunicipioAdmin(LeafletGeoAdmin):
    list_display = ['nome', 'cod_ibge_m', ]
    search_fields = ['nome', 'cod_ibge_m']

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Poco


@admin.register(Poco)
class PocoAdmin(LeafletGeoAdmin):
    # Exibição das colunas na lista
    list_display = ['proprietario', 'orgao', 'profundidade', 'q_m3h', 'equipamento', 'data_perfuracao',]
    # Adicionar filtros para melhorar a pesquisa
    search_fields = ['proprietario', 'orgao', 'equipamento']
    # Ordenação da lista de poços
    ordering = ['data_perfuracao']
    # Personalizar filtros adicionais
    list_filter = ['data_perfuracao', 'orgao']  # Filtro de data para perfuração
    # Adicionar filtros de pesquisa mais avançados
    search_fields = ('proprietario', 'orgao', 'equipamento')
    # Melhorias na interface, como a exibição de tags
    list_display_links = ('proprietario', 'orgao')



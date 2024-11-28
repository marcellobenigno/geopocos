from django.contrib.gis.db import models


class Municipio(models.Model):
    nome = models.CharField('nome', max_length=40)
    cod_ibge_m = models.CharField('código IBGE', max_length=20)
    geom = models.MultiPolygonField('geom', srid=4326)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

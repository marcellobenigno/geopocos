from django.contrib.gis.db import models
from django.template.defaultfilters import date


class Poco(models.Model):
    proprietario = models.CharField('proprietário', max_length=255, null=True, blank=True)
    orgao = models.CharField('órgão responsável', max_length=255, null=True, blank=True)
    data_perfuracao = models.DateField('data de perfuração', null=True, blank=True)
    profundidade = models.FloatField('profundidade (m)', null=True, blank=True)
    q_m3h = models.FloatField('vazão m3/h', null=True, blank=True)
    equipamento = models.CharField('equipamento', max_length=255, null=True, blank=True)
    geom = models.PointField('geom', srid=4326)

    def __str__(self):
        return self.proprietario

    class Meta:
        verbose_name = 'Poço'
        verbose_name_plural = 'Poços'

    @property
    def popup_content(self):
        popup = "<span>Proprietário: </span>{}".format(
            self.proprietario)
        popup += "<span>Órgão: </span>{}".format(
            self.orgao)
        popup += "<span>Data de Perfuração: </span>{}".format(
            date(self.data_perfuracao, "d/m/Y"))
        popup += "<span>Profundidade (m): </span>{}".format(
            self.profundidade)
        popup += "<span>Vazão (m3/h): </span>{}".format(
            self.q_m3h)
        popup += "<span>Equipamento: </span>{}".format(
            self.equipamento)
        return popup

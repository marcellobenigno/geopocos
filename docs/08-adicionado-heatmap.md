# 8. CRIANDO O MAPA DE INTENSIDADE DE PONTOS (HEATMAP)

Vamos melhorar o nosso mapa através do plugin do Leaflet chamado [Leaflet.heat](https://github.com/Leaflet/Leaflet.heat), para isso, baixe o conteúdo da pasta **dist**, que no caso é o arquivo `leaflet-heat.js`na seguinte pasta em `geopocos/geopocos/core/static/libs`:

```bash
.
├── css
│   └── main.css
├── js
│   └── jquery-3.3.1.min.js
└── libs
    ├── bootstrap-4.1.3
    ├── leaflet
    └── leaflet-heat
        └── leaflet-heat.js
```

Precisamos criar uma view que gere um array no seguinte formato:

```javascript
var heat = L.heatLayer([
	[50.5, 30.5, 0.2], // lat, lng, intensity
	[50.6, 30.4, 0.5],
	...
], {radius: 25}).addTo(map);
```

Para isso, vamos alterar o arquivo `views.py` da nossa app `poco`:

```python
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

```

O conteúdo do arquivo `poco/poco_js.html` será:

```python
var pocosCoord = [
{% for poco in object_list %}
        [{{ poco.geom.y|safe }}, {{ poco.geom.x|safe }}, {{ poco.q_m3h|safe }}],
{% endfor %}
];
```
Criamos então a url de acesso a este aquivo javascript:

```python
from django.urls import path

from . import views as v

app_name = 'poco'

urlpatterns = [
    path('geojson/', v.PocoGeoJson.as_view(), name='poco_geojson'),
    path('pocos.js/', v.pocos_js, name='pocos_js'),
]
```

Precisamos alterar a `view` da nossa app `mapa`, adicionando uma variável com o valor da vazão máxima, necessária para gerar o peso de cada ponto no mapa de intensidade:

```python
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
```

Com esta alteração, também é necessário modificar o arquivo `mapa.html`:


```html
{% extends 'base.html' %}
{% load static %}

{% block extra_css %}
    <link href="{% static 'libs/leaflet/leaflet.css' %}" rel="stylesheet">
{% endblock extra_css %}


{% block content %}
    <div id="map"></div>
    <input type="hidden" id="pocos_geojson" value="{% url 'poco:poco_geojson' %}">
    <input type="hidden" id="qmax" value="{{ q_max.q_m3h__max|safe }}">
{% endblock content %}


{% block extra_js %}
    <script src="{% static 'libs/leaflet/leaflet.js' %}"></script>
    <script src="{% static 'libs/leaflet-heat/leaflet-heat.js' %}"></script>
    <script src="{% url 'poco:pocos_js' %}"></script>
    <script>
        {% include 'includes/js/map.js' %}
    </script>
{% endblock extra_js %}
```

Para finalizar, vamos adicionar a nossa camada no arquivo `map.js`:

```javascript
function onEachFeature(feature, layer) {
    var popupContent = feature.properties.popup_content;
    layer.bindPopup(popupContent);
}

var gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var pocos = L.geoJson([], {
    style: {
        fillColor: '#ffffff',
        weight: 2,
        opacity: 1,
        color: '#000000',
        fillOpacity: 1
    },
    pointToLayer: function (feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 4});
    },
    onEachFeature: onEachFeature,
});

var poco_geojson_dataurl = $("#pocos_geojson").val();

$.getJSON(poco_geojson_dataurl, function (data) {
    // Add GeoJSON layer
    pocos.addData(data);
});

var heat = L.heatLayer(pocosCoord, {
    radius: 22,
    blur: 30,
    max: $("#qmax").val(),
    minOpacity: 0.7
});

var map = L.map('map', {
    center: [-7.166300, -36.77673],
    zoom: 8,
    layers: [gstreets, heat, pocos],
});

var baseLayers = {
    "Google Streets": gstreets,
    "Google Satélite": satellite,
};

var overlays = {
    "Poços": pocos,
    "Heat": heat,
};

var control = L.control.layers(baseLayers, overlays).addTo(map);
```


![](.pastes/2019-10-07-21-58-05.png)
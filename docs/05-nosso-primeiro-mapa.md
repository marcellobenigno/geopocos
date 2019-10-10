# 5. NOSSO PRIMEIRO MAPA 🌎

Vamos adicionar a biblioteca [Leaflet](https://leafletjs.com/) no pasta libs, dos nossos arquivos estáticos, em `geopocos/geopocos/core/static`: 
```
.
├── css
│   └── main.css
├── js
│   └── jquery-3.3.1.min.js
└── libs
    ├── bootstrap-4.1.3
    ├── leaflet
```

Em seguida, altere o arquivo `base.html`:

```html
{% load static %}

<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <title>GeoPoços</title>
    <link href="{% static 'libs/bootstrap-4.1.3/css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'css/main.css' %}" rel="stylesheet">
    {% block extra_css %}
    {% endblock extra_css %}
</head>
<body>
{% include 'includes/navbar.html' %}

<div class="container-fluid">
    {% block content %}
    {% endblock content %}
</div>
<script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
<script src="{% static 'libs/bootstrap-4.1.3/js/bootstrap.min.js' %}"></script>
{% block extra_js %}
{% endblock extra_js %}
</body>
</html>
```

Agora poderemos criar uma nova **view** que será responsável por renderizar um **template** com o nosso mapa, para isso, altere o arquivo `geopocos/geopocos/core/views/py`:

```python
from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def mapa(request):
    return render(request, 'core/mapa.html', context)
```

e o conteúdo do arquivo `geopocos/geopocos/core/mapa.html` será esse:

```html
{% extends 'base.html' %}
{% load static %}

{% block extra_css %}
    <link href="{% static 'libs/leaflet/leaflet.css' %}" rel="stylesheet">
{% endblock extra_css %}

{% block content %}
    <div id="map"></div>
{% endblock content %}

{% block extra_js %}
    <script src="{% static 'libs/leaflet/leaflet.js' %}"></script>
    <script src="{% static 'js/map.js' %}"></script>
{% endblock extra_js %}
```

Devemos então criar o arquivo `geopocos/geopocos/core/static/js/map.js`:

```javascript
var gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var map = L.map('map', {
    center: [-7.166300, -36.77673],
    zoom: 8,
    maxZoom: 20,
    layers: [gstreets],
});

var baseLayers = {
    "Google Streets": gstreets,
    "Google Satélite": satellite,
};

var overlays = {
};

var control = L.control.layers(baseLayers, overlays).addTo(map); 
```

O Leaflet precisa que a **div** `map` tenha sua altura e largura definida para poder exibir o mapa, então vamos alterar o nosso arquivo `main.css` adicionando:

```css
body {
    padding-top: 3.5rem;
}

#map {
    margin-top: 0.5rem;
    padding: 0;
    width: 100%;
    min-height: calc(100vh - 75px);
    border: 1px solid #cfcfcf;
    border-radius: 8px;
}
```

Agora, iremos criar a nossa rota no arquivo `core/urls.py`:

```python
from django.urls import path

from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('mapa/', v.mapa, name='mapa'),
]
```

**Pronto!** Reinicie o `runserver`e veja como ficou: 

```bash
m runserver
```

![](.pastes/2019-10-06-21-57-58.png)

**OBS:** Não se esqueça de criar os links para o mapa na **navbar** e na **página inicial**. 
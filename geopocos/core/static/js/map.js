const pocosCoordUrl = document.getElementById('pocos_geojson').value;

function onEachFeature(feature, layer) {
    var popupContent = feature.properties.popup_content;
    layer.bindPopup(popupContent);
}

const gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20, attribution: 'google'
});

const satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20, attribution: 'google'
});

const style = {
    fillColor: '#ffffff',
    weight: 2,
    opacity: 1,
    color: '#000000',
    fillOpacity: 1,
    radius: 4,
}

const heat = L.heatLayer([], {
    radius: 22,
    blur: 30,
    max: $("#qmax").val(),
    minOpacity:
        0.7
});

const pocos = new L.GeoJSON.AJAX(pocosCoordUrl, {
    pointToLayer: function (feature, latlng) {
        heat.addLatLng(latlng);
        return L.circleMarker(latlng, style);
    }, onEachFeature: onEachFeature
});

const map = L.map('map', {
    center: [-7.166300, -36.77673],
    zoom: 8,
    layers: [gstreets, pocos, heat],
});

const baseLayers = {
    "Google Streets": gstreets, "Google Satélite": satellite,
};

const overlays = {
    "Poços": pocos,
    "Heat": heat,
};

const control = L.control.layers(baseLayers, overlays).addTo(map);
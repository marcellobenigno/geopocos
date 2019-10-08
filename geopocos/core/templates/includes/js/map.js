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
    minOpacity:
        0.7
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
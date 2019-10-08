from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('geopocos.core.urls')),
    path('pocos/', include('geopocos.poco.urls')),
    path('admin/', admin.site.urls),
]

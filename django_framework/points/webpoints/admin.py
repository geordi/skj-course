from django.contrib.gis import admin
#from django.contrib import admin
from .models import Point

admin.site.register(Point, admin.OSMGeoAdmin)
#admin.site.register(Point)

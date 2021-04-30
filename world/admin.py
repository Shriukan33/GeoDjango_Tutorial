from django.contrib.gis import admin

# Register your models here.
from .models import WorldBorders

admin.site.register(WorldBorders, admin.OSMGeoAdmin)

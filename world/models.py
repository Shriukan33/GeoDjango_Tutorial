from django.contrib.gis.db import models

# Create your models here.

class WorldBorders(models.Model):
    # Models corresponding to the attributes within the world borders shapefile (.shp)
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS code', max_length=2, null=True) # Sort of postal code specific to a county
    iso2 = models.CharField('2 digits ISO', max_length=2) # France : FR
    iso3 = models.CharField('3 digits ISO', max_length=3) # France : FRA
    un = models.IntegerField('United Nation code') # France métropolitaine: 250
    region = models.IntegerField('Region code') # Specific to US ?
    subregion = models.IntegerField('Sub-region code') # Same, not sure
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    # A specific field to add because it's GeoDjango
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name
from django.contrib.gis import admin
from .models import Arret
from leaflet.admin import LeafletGeoAdmin

class ArretAdmin(LeafletGeoAdmin):
    # fields to show in admin listview
    list_display = ('nom_lignesBis', 'nom_arret', 'coords', 'date')

# Register your models here.
admin.site.register(Arret, ArretAdmin)
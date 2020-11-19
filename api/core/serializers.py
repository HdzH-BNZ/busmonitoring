#pr avoir des coordonnées qu'on peut catch avec Axios sur l'API, faut use DRF-gis !
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Arret

class ArretSerializers(GeoFeatureModelSerializer):
    
    class Meta():
        model = Arret
        geo_field = "coords"#obligé de définir un geofield
        fields = ("id", "nom_exploit", "nom_arret", "nom_commune", "etat_arret", "acces_pmr", "marquage_sol", "etat_marquage", "poubelle", "banc", "toit", "horaires", "carte_trajets", "comment", "img", "date", "nom_lignesBis")
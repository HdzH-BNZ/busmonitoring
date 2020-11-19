from django.db import models
from django.contrib.gis.db import models as geomodels
from multiselectfield import MultiSelectField

# Create your models here.

class Arret(models.Model):
    ARRETS_ETATS = (
        ('Dégradé', 'Dégradé'),
        ('Propre', 'Propre'),
    )
    MARQUAGE_ETATS = (
        ('Absent', 'Absent'),
        ('Usé', 'Usé'),
        ('Bon', 'Bon'),
        ('Neuf', 'Neuf'),
    )
    LISTE_LIGNES = (('ligne 10', 'ligne 10'),
                ('ligne 12', 'ligne 12'),
                ('ligne 29', 'ligne 29'),
                ('ligne 30', 'ligne 30'),
                ('ligne 36', 'ligne 36'),
                ('ligne 37E', 'ligne 37E'),
                ('ligne 38', 'ligne 38'),
                ('ligne 39', 'ligne 39'),
                ('ligne 42', 'ligne 42'),
                ('ligne 44', 'ligne 44'),
                ('ligne 45', 'ligne45'),
                ('ligne 48A', 'ligne 48A'),
                ('ligne 48B', 'ligne 48B'),
                ('ligne 48AB', 'ligne 48AB'),
                ('ligne 48C', 'ligne 48C'),
                ('ligne 49', 'ligne 49'),
                ('ligne 56', 'ligne 56'),
                ('ligne 57', 'ligne 57'),
                ('ligne 58', 'ligne 58'),
                ('ligne 59', 'ligne 59'),
                ('ligne 60', 'ligne 60'),
                ('ligne 95-03A', 'ligne 95-03A'),
                ('ligne 95-03B', 'ligne 95-03B'),
                ('ligne 95-04', 'ligne 95-04'),
                ('ligne 95-05', 'ligne 95-05'),
                ('ligne 95-06', 'ligne 95-06'),
                ('ligne 95-07', 'ligne 95-07'),
                ('ligne 95-08', 'ligne 95-08'),
                ('ligne 95-12', 'ligne 95-12'),
                ('ligne 95-17', 'ligne 95-17'),
                ('ligne 95-18', 'ligne 95-18'),
                ('ligne 95-19', 'ligne 95-19'),
                ('ligne 95-20', 'ligne 95-20'),
                ('ligne 95-22', 'ligne 95-22'),
                ('ligne 95-23', 'ligne 95-23'),
                ('ligne 95-41', 'ligne 95-41'),
                ('ligne 95-48', 'ligne 95-48'),
                ('ligne EXPRESS-16', 'ligne EXPRESS-16'),
                ('ligne EXPRESS-27', 'ligne EXPRESS-27'),
                ('ligne EXPRESS-80', 'ligne EXPRESS-80'),
                ('ligne N150', 'ligne N150'),
                ('ligne N152', 'ligne N152'),
                ('', ''))
    id = models.AutoField(primary_key=True)#peut-être inutile de le mettre
    nom_lignesBis = MultiSelectField(choices=LISTE_LIGNES,
                                max_choices=10,
                                max_length=100)
    nom_exploit = models.CharField(max_length=50)
    nom_arret = models.CharField(max_length=50)
    nom_commune = models.CharField(max_length=50)
    etat_arret = models.CharField(choices=ARRETS_ETATS, max_length=100)
    acces_pmr = models.BooleanField()
    marquage_sol = models.BooleanField()
    etat_marquage = models.CharField(choices=MARQUAGE_ETATS, max_length=50)
    poubelle = models.BooleanField()
    banc = models.BooleanField(default=False)
    toit = models.BooleanField(default=False)
    horaires = models.BooleanField(default=False)
    carte_trajets = models.BooleanField(default=False)
    comment = models.CharField(default='aucun commentaire', max_length=100)
    img = models.FileField()
    coords = geomodels.PointField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nom_arret
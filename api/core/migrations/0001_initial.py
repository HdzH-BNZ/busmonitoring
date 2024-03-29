# Generated by Django 3.1.3 on 2020-11-10 17:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arret',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_exploit', models.CharField(max_length=50)),
                ('nom_arret', models.CharField(max_length=50)),
                ('nom_ligne', models.CharField(max_length=50)),
                ('nom_commune', models.CharField(max_length=50)),
                ('etat_arret', models.CharField(choices=[('Dégradé', 'Dégradé'), ('Propre', 'Propre')], max_length=100)),
                ('equipement', models.CharField(max_length=50)),
                ('acces_pmr', models.BooleanField()),
                ('marquage_sol', models.BooleanField()),
                ('etat_marquage', models.CharField(choices=[('Absent', 'Absent'), ('Usé', 'Usé'), ('Bon', 'Bon'), ('Neuf', 'Neuf')], max_length=50)),
                ('poubelle', models.BooleanField()),
                ('img', models.FileField(upload_to='')),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]

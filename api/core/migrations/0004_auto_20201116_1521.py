# Generated by Django 3.1.3 on 2020-11-16 14:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_arret_nom_lignebis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arret',
            name='nom_ligneBis',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ligne 49', 'ligne 49'), ('ligne 56', 'ligne 56'), ('ligne 58', 'ligne 58'), ('ligne 9519A', 'ligne 9519A'), ('ligne 9519B', 'ligne 9519B')], max_length=15),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-17 07:49

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201116_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arret',
            name='nom_ligne',
        ),
        migrations.RemoveField(
            model_name='arret',
            name='nom_ligneBis',
        ),
        migrations.AddField(
            model_name='arret',
            name='lignes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ligne 10', 'ligne 10'), ('ligne 12', 'ligne 12'), ('ligne 29', 'ligne 29'), ('ligne 30', 'ligne 30'), ('ligne 36', 'ligne 36'), ('ligne 37E', 'ligne 37E'), ('ligne 38', 'ligne 38'), ('ligne 39', 'ligne 39'), ('ligne 42', 'ligne 42'), ('ligne 44', 'ligne 44'), ('ligne 45', 'ligne 45'), ('ligne 48A', 'ligne 48A'), ('ligne 48B', 'ligne 48B'), ('ligne 48AB', 'ligne 48AB'), ('ligne 48C', 'ligne 48C'), ('ligne 49', 'ligne 49'), ('ligne 56', 'ligne 56'), ('ligne 57', 'ligne 57'), ('ligne 58', 'ligne 58'), ('ligne 59', 'ligne 59'), ('ligne 60', 'ligne 60'), ('ligne 95-03A', 'ligne 95-03A'), ('ligne 95-03B', 'ligne 95-03B'), ('ligne 95-04', 'ligne 95-04'), ('ligne 95-05', 'ligne 95-05'), ('ligne 95-06', 'ligne 95-06'), ('ligne 95-07', 'ligne 95-07'), ('ligne 95-08', 'ligne 95-08'), ('ligne 95-12', 'ligne 95-12'), ('ligne 95-17', 'ligne 95-17'), ('ligne 95-18', 'ligne 95-18'), ('ligne 95-19', 'ligne 95-19'), ('ligne 95-20', 'ligne 95-20'), ('ligne 95-22', 'ligne 95-22'), ('ligne 95-23', 'ligne 95-23'), ('ligne 95-41', 'ligne 95-41'), ('ligne 95-48', 'ligne 95-48'), ('ligne EXPRESS-16', 'ligne EXPRESS-16'), ('ligne EXPRESS-27', 'ligne EXPRESS-27'), ('ligne EXPRESS-80', 'ligne EXPRESS-80'), ('ligne N150', 'ligne N150'), ('ligne N152', 'ligne N152')], default=0, max_length=100),
            preserve_default=False,
        ),
    ]
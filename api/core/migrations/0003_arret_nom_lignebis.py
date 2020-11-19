# Generated by Django 3.1.3 on 2020-11-16 13:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201111_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='arret',
            name='nom_ligneBis',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'ligne 49'), (2, 'ligne 56'), (3, 'ligne 58'), (4, 'ligne 9519A'), (5, 'ligne 9519B')], default=0, max_length=3),
            preserve_default=False,
        ),
    ]
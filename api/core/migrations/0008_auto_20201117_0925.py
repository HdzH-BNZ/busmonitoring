# Generated by Django 3.1.3 on 2020-11-17 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201117_0849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arret',
            old_name='lignes',
            new_name='list_lignes',
        ),
    ]

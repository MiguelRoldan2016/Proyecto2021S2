# Generated by Django 3.2.7 on 2021-10-26 05:12

import biblioteca.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_auto_20211025_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(default='https://bibliotecapictures.s3.amazonaws.com/static/default.png', storage=biblioteca.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='default.png', storage=biblioteca.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]

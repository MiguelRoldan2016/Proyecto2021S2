# Generated by Django 3.2.7 on 2021-10-26 01:27

import biblioteca.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0014_auto_20211025_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(default='https://bibliotecapictures.s3.amazonaws.com/static/default.png', upload_to=biblioteca.storage_backends.PublicMediaStorage()),
        ),
        migrations.AlterField(
            model_name='historicalautor',
            name='imagen',
            field=models.TextField(default='https://bibliotecapictures.s3.amazonaws.com/static/default.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to=biblioteca.storage_backends.PublicMediaStorage()),
        ),
    ]

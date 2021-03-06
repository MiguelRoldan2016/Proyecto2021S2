# Generated by Django 3.2.7 on 2021-10-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0016_auto_20211025_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(default='https://bibliotecapictures.s3.amazonaws.com/static/default.png', upload_to='https://bibliotecapictures.s3.amazonaws.com/media/autores/'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to='https://bibliotecapictures.s3.amazonaws.com/media/publicaciones/'),
        ),
    ]

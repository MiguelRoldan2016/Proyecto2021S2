# Generated by Django 3.2.7 on 2021-10-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_alter_ejemplar_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(default='/static/default.png', upload_to='media/publicaciones/'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='/static/default.png', upload_to='media/publicaciones/'),
        ),
    ]

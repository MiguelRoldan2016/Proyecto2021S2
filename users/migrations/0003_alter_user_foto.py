# Generated by Django 3.2.7 on 2021-10-25 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='/static/default.png', upload_to='profile_pics/'),
        ),
    ]
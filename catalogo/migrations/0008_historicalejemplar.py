# Generated by Django 3.2.7 on 2021-10-08 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0007_delete_historicalejemplar'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalEjemplar',
            fields=[
                ('ip_address', models.GenericIPAddressField(verbose_name='IP address')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, help_text='Identificador unico para este ejemplar')),
                ('impresion', models.CharField(max_length=200)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('disponibilidad', models.CharField(blank=True, choices=[('m', 'Mantenimiento'), ('p', 'Prestado'), ('d', 'Disponible'), ('r', 'Reservado'), ('x', 'Solo consulta')], default='m', help_text='Disponibilidad de este ejemplar', max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('prestado_a', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('publicacion', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='catalogo.publicacion')),
            ],
            options={
                'verbose_name': 'historical Ejemplar',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

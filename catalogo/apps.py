from django.apps import AppConfig
from simple_history.signals import pre_create_historical_record
from .signals import add_history_ip_address


class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogo'

    def ready(self):
        pre_create_historical_record.connect(
            add_history_ip_address,
            sender=self
        )

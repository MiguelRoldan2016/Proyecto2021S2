from simple_history.models import HistoricalRecords
from simple_history.signals import pre_create_historical_record
from django.dispatch import receiver


@receiver(pre_create_historical_record)
def add_history_ip_address(sender, **kwargs):
    try:
        history_instance = kwargs['history_instance']
        history_instance.ip_address = HistoricalRecords.context.request.META['REMOTE_ADDR']
    except AttributeError:
        return

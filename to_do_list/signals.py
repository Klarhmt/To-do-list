from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from . import models

@receiver(pre_save,sender=models.Task)
def set_urgent_status(sender,instance,**kwargs):
    time_difference = instance.due_by_date - timezone.now().date()
    if time_difference.days <7:
        instance.is_it_urgent = 'Y'
    else:
        instance.is_it_urgent = 'N'
from django.db import models
from smartmin.models import SmartModel
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save

from datetime import datetime, timedelta

class Opportunity(SmartModel):
    title = models.CharField(max_length=128,
                             help_text="A title for the opportunity")
    description = models.TextField(max_length=2048,
                                   help_text="A summary of the opportunity in 2000 caracters")
    link = models.CharField(max_length=256,
                            help_text="Provide a link if possible", blank=True, null=True)

    remaining_days = models.IntegerField(default=0, 
                                   help_text="Number of days remaining before expiration, leave it blank for unlimited")

    deadline = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Opportunities"

@receiver(pre_save, sender=Opportunity)
def pre_save_opportunity(sender, instance, **kwargs):
    if instance.link.strip() == "":
        instance.link = None
    elif instance.link[:8] != 'http://' and instance.link.strip() != "":
        instance.link = 'http://' + instance.link
    

    instance.link = instance.link
    
    if instance.remaining_days > 0:
        if not instance.created_on:
            instance.created_on = timezone.now()
        deadline = instance.created_on + timedelta(days=instance.remaining_days)
        instance.deadline = deadline.date()
    else:
        instance.deadline = None
        

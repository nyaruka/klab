from django.core.cache import get_cache
from django.db import models
from django.conf import settings
from smartmin.models import SmartModel

import flickr
from datetime import datetime, timedelta

class Event(SmartModel):
    """
    The blueprint of events
    """
    RECURRENCE_CHOICES = (
        ('W', "Weekly"),
        ('M', "Monthly"),
        )

    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    date = models.DateField(help_text="The date when the event will occur")
    time = models.TimeField(help_text="The start time for the event")
    duration = models.IntegerField(help_text="The duration in minutes of the event")
    title = models.CharField(max_length=64,
                                   help_text="What is the title of this event")
    logo = models.ImageField(upload_to="photos/", help_text="The image representing the event in general (should be square)")
    description = models.TextField(max_length=256,
                                   help_text="More descriptively say about this event")
    venue = models.CharField(max_length=128,
                             help_text="The exact location where event will take place")
    
    recurrence_type = models.CharField(max_length=1, choices=RECURRENCE_CHOICES, null=True, blank=True,
                                   help_text="Does this event accur weekly or monthly")
    dow = models.IntegerField(null=True, blank=True)
    monthly_ordinal = models.IntegerField(null=True, blank=True)
    photo_tag = models.CharField(max_length=64, null=True, blank=True)
    end_date = models.DateField(help_text="Last date of recurrence", null=True, blank=True)
  
    def get_duration(self):
        if self.duration <= 120:
            return "%d minutes" % self.duration
        elif self.duration <= 1440:
            hours = self.duration / 60
            return "%d hours" % hours
        else:
            days = self.duration / 1440
            return "%d days" % days


    def __unicode__(self):
        return self.title

    def get_cache_key(self):
        return 'flickr_event_photos_%d' % self.pk

    def photos(self):
        if self.photo_tag:
        
            # try to get flickr photos with a given tag
            try:
                cache = get_cache('default')
                key = self.get_cache_key()

                if not cache.get(key):
                    event_photos = flickr.api.walk(user_id=flickr.user_id, tags=self.photo_tag) 
                    cache.set(key, list(iter(event_photos)), 3600)

                event_photos = cache.get(key)

                return event_photos
            except:
                # otherwise give back nothing
                return None

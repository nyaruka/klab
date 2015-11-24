# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markdown


class Migration(migrations.Migration):

    def markdownify_events(apps, schema_editor):
        Event = apps.get_model('events', "Event")
        for event in Event.objects.all():
            description = event.description
            if not description.startswith('<'):
                event.description = markdown.markdown(description)
                event.save()

    dependencies = [
        ('events', '0002_auto_20150126_2027'),
    ]

    operations = [
        migrations.RunPython(markdownify_events),
    ]

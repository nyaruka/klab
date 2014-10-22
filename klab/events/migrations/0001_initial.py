# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('date', models.DateField(help_text=b'The date when the event will occur')),
                ('time', models.TimeField(help_text=b'The start time for the event')),
                ('duration', models.IntegerField(help_text=b'The duration in minutes of the event')),
                ('title', models.CharField(help_text=b'What is the title of this event', max_length=64)),
                ('logo', models.ImageField(help_text=b'The image representing the event in general (should be square)', upload_to=b'photos/')),
                ('description', models.TextField(help_text=b'More descriptively say about this event', max_length=256)),
                ('venue', models.CharField(help_text=b'The exact location where event will take place', max_length=128)),
                ('recurrence_type', models.CharField(blank=True, max_length=1, null=True, help_text=b'Does this event accur weekly or monthly', choices=[(b'W', b'Weekly'), (b'M', b'Monthly')])),
                ('dow', models.IntegerField(null=True, blank=True)),
                ('monthly_ordinal', models.IntegerField(null=True, blank=True)),
                ('photo_tag', models.CharField(max_length=64, null=True, blank=True)),
                ('end_date', models.DateField(help_text=b'Last date of recurrence', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name=b'events_event_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name=b'events_event_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('parent', models.ForeignKey(related_name=b'children', blank=True, to='events.Event', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(help_text=b'The name of the video', max_length=255)),
                ('summary', models.TextField(help_text=b'A short blurb about the video')),
                ('description', models.TextField(help_text=b'The full description for the video')),
                ('youtube_id', models.CharField(help_text=b'The id youtube uses for this video', max_length=255)),
                ('created_by', models.ForeignKey(related_name=b'events_video_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name=b'events_video_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

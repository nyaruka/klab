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
            name='Opportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('title', models.CharField(help_text=b'A title for the opportunity', max_length=128)),
                ('description', models.TextField(help_text=b'A summary of the opportunity in 2000 caracters', max_length=2048)),
                ('link', models.CharField(help_text=b'Provide a link if possible', max_length=256, null=True, blank=True)),
                ('remaining_days', models.IntegerField(default=0, help_text=b'Number of days remaining before expiration, leave it blank for unlimited')),
                ('deadline', models.DateField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name=b'opportunities_opportunity_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name=b'opportunities_opportunity_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
            },
            bases=(models.Model,),
        ),
    ]

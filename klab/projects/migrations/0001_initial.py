# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('title', models.CharField(help_text=b'The title of the project', max_length=64)),
                ('description', models.TextField(help_text=b'Reviewed description of the project, this will be published on the website', max_length=2048)),
                ('logo', models.ImageField(help_text=b'A logo for your project', null=True, upload_to=b'projects/logos', blank=True)),
                ('created_by', models.ForeignKey(related_name=b'projects_project_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name=b'projects_project_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('owner', models.ForeignKey(help_text=b'The owner of the project', to='members.Member')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

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
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text='When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text='When this item was last modified', auto_now=True)),
                ('title', models.CharField(help_text='Meaningful one line explenation', max_length=128)),
                ('body', models.TextField(help_text='Detailed content of the post')),
                ('image_id', models.CharField(help_text='The flickr image id tagged blog', max_length=128)),
                ('created_by', models.ForeignKey(related_name='blog_post_creations', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text='The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='blog_post_modifications', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text='The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

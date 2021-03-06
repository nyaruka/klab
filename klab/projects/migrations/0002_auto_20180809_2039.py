# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-09 18:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.PROTECT, related_name='projects_project_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was originally created'),
        ),
        migrations.AlterField(
            model_name='project',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.PROTECT, related_name='projects_project_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='modified_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was last modified'),
        ),
    ]

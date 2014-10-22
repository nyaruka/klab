# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('projects', '__first__'),

    ]

    operations = [
        migrations.RunSQL("",
                          None,
                          [
                              migrations.AddField(
                                  model_name='member',
                                  name='projects',
                                  field=models.ManyToManyField(to='projects.Project', null=True, blank=True),
                                  ),
                          ])
    ]

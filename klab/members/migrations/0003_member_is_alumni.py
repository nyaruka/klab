# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20141022_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_alumni',
            field=models.BooleanField(default=False, help_text='Member has became an Alumni'),
            preserve_default=True,
        ),
    ]

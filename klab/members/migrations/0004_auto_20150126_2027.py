# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_is_alumni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_type',
            field=models.CharField(help_text='The type of membership', max_length=1, choices=[(b'G', b'Green - kLab Tenant'), (b'B', b'Blue - kLab Mentor'), (b'R', b'Red - kLab Core Team')]),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20150126_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='location',
            field=models.CharField(default='KIGALI', help_text='kLab location your are applying for.', max_length=64, choices=[(b'KIGALI', b'Kigali'), (b'KIGALI/KINYINYA', b'Kigali Kinyinya (For under 15 years ONLY)'), (b'KARONGI', b'Karongi'), (b'RUBAVU', b'Rubavu'), (b'RUSIZI', b'Rusizi'), (b'MUSANZE', b'Musanze'), (b'HUYE', b'Huye'), (b'MUHANGA', b'Muhanga'), (b'NYAGATARE', b'Nyagatare'), (b'RWAMAGANA', b'Rwamagana')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='location',
            field=models.CharField(default='KIGALI', help_text='kLab location choosen', max_length=64),
            preserve_default=True,
        ),
    ]

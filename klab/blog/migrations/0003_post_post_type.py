# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151106_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(default=b'B', help_text=b'Whether this post is a blog post or a startup', max_length=1, choices=[(b'B', b'Blog'), (b'S', b'Startup')]),
            preserve_default=True,
        ),
    ]

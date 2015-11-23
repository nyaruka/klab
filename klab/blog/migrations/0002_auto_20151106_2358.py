# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markdown


class Migration(migrations.Migration):

    def markdownify_posts(apps, schema_editor):
        Post = apps.get_model('blog', "Post")
        for post in Post.objects.all():
            body = post.body
            if not body.startswith('<'):
                post.body = markdown.markdown(body)
                post.save()

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(markdownify_posts),
    ]

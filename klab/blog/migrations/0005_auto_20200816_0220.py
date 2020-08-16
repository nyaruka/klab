# Generated by Django 2.0.13 on 2020-08-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180809_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('B', 'Blog'), ('S', 'Startup')], default='B', help_text='Whether this post is a blog post or a startup', max_length=1),
        ),
    ]
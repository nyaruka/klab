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
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text='When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text='When this item was last modified', auto_now=True)),
                ('first_name', models.CharField(help_text='Your first (given) name', max_length=64)),
                ('last_name', models.CharField(help_text='Your last (family) name', max_length=64)),
                ('phone', models.CharField(help_text='Your phone number (including country code) - eg: 250788123456', max_length=12)),
                ('email', models.EmailField(help_text='Your email address', max_length=75)),
                ('picture', models.ImageField(help_text='A close-up photo of yourself', upload_to='members/application')),
                ('country', models.CharField(help_text='The country you live in - eg: Rwanda', max_length=18)),
                ('city', models.CharField(help_text='The city you live in - eg: Kigali', max_length=18)),
                ('neighborhood', models.CharField(help_text='The neighborhood you live in - eg: Nyamirambo', max_length=26)),
                ('professional_status', models.CharField(help_text='Your professional background', max_length=3, choices=[(b'STU', b'Student'), (b'ENT', b'Entrepreneur'), (b'EIT', b'Employed in IT'), (b'NIT', b'Employed in non-IT'), (b'UNE', b'Not currently employed')])),
                ('applying_for', models.CharField(help_text='The type of membership you are applying for', max_length=1, choices=[(b'G', b'Green - kLab Tenant'), (b'B', b'Blue - kLab Mentor')])),
                ('frequency', models.CharField(help_text='How often you plan on visiting kLab', max_length=1, choices=[(b'D', b'Daily'), (b'W', b'A few times a week'), (b'M', b'A few times a month')])),
                ('goals', models.TextField(help_text='If you are applying as a tenant, please tell us what your ongoing projects are and how you see kLab helping to accomplish your goals. If you are applying as a mentor, please tell us what you have to offer the kLab community, and what your goals are as a mentor (1024 character limit).', max_length=1024)),
                ('education', models.TextField(help_text='Your education, including any degrees or certifications earned (1024 character limit).', max_length=1024)),
                ('experience', models.TextField(help_text='Briefly describe your experience, projects you have worked on, and companies you have worked for. Please include the URLs of any projects you worked on and how you contributed (1024 character limit).', max_length=1024)),
                ('created_by', models.ForeignKey(related_name='members_application_creations', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text='The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='members_application_modifications', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text='The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text='When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text='When this item was last modified', auto_now=True)),
                ('first_name', models.CharField(help_text='Your first (given) name', max_length=64)),
                ('last_name', models.CharField(help_text='Your last (family) name', max_length=64)),
                ('phone', models.CharField(help_text='Your phone number (including country code) - eg: 250788123456', max_length=12)),
                ('membership_type', models.CharField(help_text='The type of membership', max_length=1, choices=[(b'G', b'Green - kLab Tenant'), (b'B', b'Blue - kLab Mentor')])),
                ('email', models.EmailField(help_text='Your email address', max_length=75)),
                ('picture', models.ImageField(help_text='A close-up photo of yourself', upload_to='members/member/')),
                ('country', models.CharField(help_text='The country you live in - eg: Rwanda', max_length=18)),
                ('city', models.CharField(help_text='The city you live in - eg: Kigali', max_length=18)),
                ('neighborhood', models.CharField(help_text='The neighborhood you live in - eg: Nyamirambo', max_length=26)),
                ('education', models.TextField(help_text='Your education, including any degrees or certifications earned (1024 character limit).', max_length=1024)),
                ('experience', models.TextField(help_text='Briefly describe your experience, projects you have worked on, and companies you have worked for. Please include the URLs of any projects you worked on and how you contributed (1024 character limit).', max_length=1024)),
                ('token', models.CharField(help_text='token used to activate account', unique=True, max_length=32)),
                ('application', models.ForeignKey(help_text='The initial Application of the member', on_delete=models.deletion.PROTECT, to='members.Application')),
                ('created_by', models.ForeignKey(related_name='members_member_creations', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text='The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='members_member_modifications', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text='The user which last modified this item')),
                ('user', models.ForeignKey(help_text='The user account associated with this member', on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

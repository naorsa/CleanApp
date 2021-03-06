# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-18 20:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0030_auto_20170913_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]

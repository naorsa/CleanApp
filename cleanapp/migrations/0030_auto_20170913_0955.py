# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-13 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0029_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.ManyToManyField(to='cleanapp.CityModel'),
        ),
    ]

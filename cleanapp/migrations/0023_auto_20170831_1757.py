# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0022_auto_20170831_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='/Users/user/Desktop/DjangoProjects/yesPlanet/uploads/No_image_3x4.svg.png', null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
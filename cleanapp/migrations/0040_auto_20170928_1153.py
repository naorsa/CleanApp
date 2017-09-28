# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-28 11:53
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0039_auto_20170925_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='uploads/No_image_3x4.svg.png', null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
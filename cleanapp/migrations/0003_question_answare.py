# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-27 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0002_auto_20170827_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answare',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='cleanapp.Answare'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-30 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0013_auto_20170829_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answare',
            field=models.ManyToManyField(related_name='answare', to='cleanapp.Answare'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='questions',
            field=models.ManyToManyField(default=False, related_name='questions', to='cleanapp.Question'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0007_auto_20170827_2332'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='answare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cleanapp.Answare'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-25 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanapp', '0038_userprofile_perm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='perm',
            new_name='admin',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-08-05 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raspberry',
            name='user',
        ),
    ]

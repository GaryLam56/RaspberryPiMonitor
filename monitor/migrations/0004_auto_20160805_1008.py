# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-08-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20160805_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberry',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]

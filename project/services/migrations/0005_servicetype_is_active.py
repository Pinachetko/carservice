# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-13 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20170613_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
    ]

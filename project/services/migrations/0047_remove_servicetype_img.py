# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0046_auto_20170620_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetype',
            name='img',
        ),
    ]

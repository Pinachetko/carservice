# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0042_auto_20170618_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='shortcut',
            field=models.CharField(default='shortcut', max_length=100, verbose_name='Короткое имя'),
        ),
    ]
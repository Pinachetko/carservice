# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-23 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='from_date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Время отправления'),
        ),
    ]
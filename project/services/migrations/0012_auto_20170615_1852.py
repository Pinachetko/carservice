# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-15 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20170615_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetype',
            name='serviced_cars',
        ),
        migrations.AddField(
            model_name='servicetype',
            name='serviced_cars',
            field=models.ManyToManyField(blank=True, null=True, to='services.ServicedCar', verbose_name='Обслуживаемые авто'),
        ),
    ]

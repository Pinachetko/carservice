# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-17 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_auto_20170617_2008'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Anticor',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_type',
        ),
        migrations.RemoveField(
            model_name='service',
            name='serviced_cars',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='serviced_cars',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServicedCar',
        ),
        migrations.DeleteModel(
            name='ServiceType',
        ),
    ]

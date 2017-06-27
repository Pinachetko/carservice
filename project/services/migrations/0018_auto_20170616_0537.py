# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-16 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_service'),
    ]

    operations = [
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
            name='ServiceType',
        ),
    ]

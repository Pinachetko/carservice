# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-16 03:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20170615_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceType', verbose_name='Тип услуги'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-15 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_servicetype_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_cost',
            field=models.CharField(default='Договрная', max_length=100, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_name',
            field=models.CharField(default='Наименование услуга', max_length=500, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceType', verbose_name='Тип услуги'),
        ),
    ]

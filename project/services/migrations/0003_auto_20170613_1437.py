# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-13 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20170613_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='serviced_cars',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServicedCar', verbose_name='Обслуживаемые авто'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='type_name',
            field=models.CharField(default='Тип услуги', max_length=500, unique=True, verbose_name='Название'),
        ),
    ]

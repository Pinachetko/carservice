# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-13 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='serviced_cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ServicedCar', verbose_name='Обслуживаемые авто'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-17 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_anticor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='serviced_cars',
        ),
        migrations.AddField(
            model_name='service',
            name='serviced_cars',
            field=models.ManyToManyField(blank=True, null=True, to='services.ServicedCar', verbose_name='Тип автомобиля'),
        ),
    ]
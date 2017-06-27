# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-17 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0023_auto_20170617_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anticor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(default='Тип авто', max_length=500, verbose_name='Тип автомобиля')),
                ('means', models.CharField(blank=True, default='ТАНТАЛ', max_length=50, null=True, verbose_name='Средство')),
                ('service', models.CharField(default='Наименование услуга', max_length=500, verbose_name='Название')),
                ('cost', models.CharField(default='Договрная', max_length=100, verbose_name='Стоимость')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Антикоррозионная обработка',
                'db_table': 'Anticor',
                'verbose_name_plural': 'Антикоррозионные обработки',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(default='Наименование услуга', max_length=500, verbose_name='Название')),
                ('service_cost', models.CharField(default='Договрная', max_length=100, verbose_name='Стоимость')),
                ('service_description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Услуга',
                'db_table': 'Service',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServicedCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(default='Тип авто', max_length=500, unique=True, verbose_name='Тип автомобиля')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Обслуживаемый автомобиль ',
                'db_table': 'ServicedCar',
                'verbose_name_plural': 'Обслуживаемые автомобили',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default='Тип услуги', max_length=500, unique=True, verbose_name='Название')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('serviced_cars', models.ManyToManyField(blank=True, null=True, to='services.ServicedCar', verbose_name='Обслуживаемые авто')),
            ],
            options={
                'verbose_name': 'Тип услуги',
                'db_table': 'ServiceType',
                'verbose_name_plural': 'Типы услуг',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceType', verbose_name='Тип услуги'),
        ),
        migrations.AddField(
            model_name='service',
            name='serviced_cars',
            field=models.ManyToManyField(blank=True, null=True, to='services.ServicedCar', verbose_name='Тип автомобиля'),
        ),
    ]
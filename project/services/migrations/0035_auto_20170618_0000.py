# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0034_auto_20170617_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=500, verbose_name='Название материала')),
                ('material_description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name_plural': 'Используемые материалы',
                'verbose_name': 'Используемый материал',
                'db_table': 'MaterialUsed',
            },
        ),
        migrations.DeleteModel(
            name='Anticor',
        ),
        migrations.AddField(
            model_name='service',
            name='materials_used',
            field=models.ManyToManyField(blank=True, null=True, to='services.MaterialUsed', verbose_name='Используемые материалы'),
        ),
    ]

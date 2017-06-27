# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0037_auto_20170618_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='materials_used',
        ),
        migrations.AddField(
            model_name='service',
            name='material_used',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.MaterialUsed', verbose_name='Используемый материал'),
        ),
    ]
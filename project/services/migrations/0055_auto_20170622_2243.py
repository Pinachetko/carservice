# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0054_auto_20170621_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='image',
            field=models.CharField(blank=True, default='image_07.img', max_length=100, null=True, verbose_name='Название картинки'),
        ),
    ]

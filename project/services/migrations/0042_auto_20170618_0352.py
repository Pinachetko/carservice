# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0041_servicetype_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='img',
            field=models.CharField(default='image_07.jpg', max_length=100, verbose_name='Изображение'),
        ),
    ]
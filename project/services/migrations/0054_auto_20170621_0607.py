# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0053_auto_20170621_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='image',
            field=models.FilePathField(match='.+', path='/static/images/samples/390x260/', verbose_name='Изображение для раздела'),
        ),
    ]

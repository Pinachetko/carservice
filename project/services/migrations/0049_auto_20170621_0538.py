# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0048_servicetype_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='image',
            field=models.FilePathField(match='*.jpg', path='/static/images/samples/390x260', recursive=True),
        ),
    ]

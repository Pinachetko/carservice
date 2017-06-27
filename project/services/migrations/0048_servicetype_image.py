# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0047_remove_servicetype_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='image',
            field=models.FilePathField(default='/static/images/', path='/static/images', recursive=True),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-19 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180619_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]

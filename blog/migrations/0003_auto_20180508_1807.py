# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180508_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogtype',
            old_name='blog_type',
            new_name='type_name',
        ),
    ]
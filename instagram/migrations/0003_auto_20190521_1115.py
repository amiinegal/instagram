# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20190521_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_path',
        ),
    ]

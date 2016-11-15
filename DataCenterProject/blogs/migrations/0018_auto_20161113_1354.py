# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-13 11:54
from __future__ import unicode_literals

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_auto_20161106_1317'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rac',
            new_name='Rack',
        ),
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(default='UnKnown', max_length=30, primary_key=True, serialize=False, validators=[blogs.models.validate_server]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-06 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20161024_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(default='UnKnown', max_length=30, primary_key=True, serialize=False),
        ),
    ]
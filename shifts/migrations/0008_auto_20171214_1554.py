# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0007_auto_20171214_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='shift_name',
            field=models.CharField(blank=True, choices=[('Morning shift', 'Morning Shift'), ('Evening shift', 'Evening Shift'), ('Night shift', 'Night Shift')], max_length=20, null=True),
        ),
    ]

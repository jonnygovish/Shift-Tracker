# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='shift_name',
            field=models.CharField(blank=True, choices=[('Ms', 'Morning Shift'), ('Es', 'Evening Shift'), ('Ns', 'Night Shift')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='hours',
            field=models.DurationField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0008_auto_20171214_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='day_of_the_week',
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thusrday'), ('Friday', 'Friday')], max_length=20, null=True),
        ),
    ]

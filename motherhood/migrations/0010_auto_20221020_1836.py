# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-10-20 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motherhood', '0009_report_total_cost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nanny',
            new_name='Driver',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='nanny_first_name',
            new_name='driver_first_name',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='nanny_last_name',
            new_name='driver_last_name',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='nanny_phonenumber',
            new_name='driver_phonenumber',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='nanny_rate',
            new_name='driver_rate',
        ),
    ]

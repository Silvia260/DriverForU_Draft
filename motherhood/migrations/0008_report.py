# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-07 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('motherhood', '0007_auto_20220331_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('nanny_first_name', models.CharField(max_length=60)),
                ('nanny_last_name', models.CharField(max_length=60)),
                ('nanny_phonenumber', models.IntegerField()),
                ('nanny_rate', models.IntegerField()),
                ('client_id', models.IntegerField()),
                ('client_first_name', models.CharField(max_length=60)),
                ('client_last_name', models.CharField(max_length=60)),
                ('booked_hours', models.IntegerField()),
                ('payment_status', models.CharField(default='Completed', editable=False, max_length=200)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
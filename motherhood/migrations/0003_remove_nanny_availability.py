# Generated by Django 2.2 on 2022-03-23 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motherhood', '0002_auto_20220323_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nanny',
            name='availability',
        ),
    ]

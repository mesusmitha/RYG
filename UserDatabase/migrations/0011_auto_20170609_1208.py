# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDatabase', '0010_auto_20170609_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide_details',
            name='aboutguide',
            field=models.CharField(default='', max_length=210),
        ),
        migrations.AlterField(
            model_name='spons_details',
            name='aboutsponsor',
            field=models.CharField(default='', max_length=210),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserDatabase', '0014_auto_20170610_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_image',
            new_name='certificate',
        ),
    ]
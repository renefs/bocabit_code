# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeapp', '0004_auto_20171110_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='goal',
            new_name='code',
        ),
    ]

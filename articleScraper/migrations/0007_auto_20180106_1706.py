# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleScraper', '0006_auto_20180106_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revision',
            options={'ordering': ['-timestamp']},
        ),
    ]

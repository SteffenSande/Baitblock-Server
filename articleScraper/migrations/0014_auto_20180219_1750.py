# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-19 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleScraper', '0013_auto_20180219_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleurltemplate',
            options={'ordering': ['-placement']},
        ),
        migrations.AddField(
            model_name='articleurltemplate',
            name='placement',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

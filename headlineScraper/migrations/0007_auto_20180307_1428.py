# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-07 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headlineScraper', '0006_headline_url_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headlinerevision',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='headlinerevision',
            name='file',
            field=models.FilePathField(blank=True, path='/home/sindre/Documents/NewsEnhancer/sites'),
        ),
        migrations.AddField(
            model_name='headlinerevision',
            name='version',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='headlinerevision',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]

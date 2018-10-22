# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 22:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('headlineScraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('headline', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='headlineScraper.Headline')),
                ('category', models.CharField(choices=[('ARTICLE', 'Article'), ('FEED', 'Feed'), ('EXTERNAL', 'External'), ('VIDEO', 'Video')], default='ARTICLE', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2500)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('journalist', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('published', models.CharField(max_length=255)),
                ('updated', models.CharField(max_length=255)),
                ('image_attribute', models.CharField(default='src', max_length=255)),
                ('image_text', models.CharField(max_length=255)),
                ('image_photographer', models.CharField(blank=True, max_length=255)),
                ('image_element', models.CharField(max_length=255)),
                ('photographer_delimiter', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), blank=True, default=list, size=None)),
                ('photograph_ignore_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), blank=True, default=list, size=None)),
                ('ignore_content_tag', models.CharField(blank=True, max_length=255)),
                ('subscription', models.CharField(blank=True, max_length=255)),
                ('video', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(null=True)),
                ('file', models.FilePathField(blank=True, path='/Users/sindre/Developer/Git/Bitbucket/master/articles')),
                ('version', models.IntegerField()),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
                ('words', models.IntegerField()),
                ('subscription', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleScraper.Article')),
                ('images', models.ManyToManyField(to='articleScraper.ArticleImage')),
                ('journalists', models.ManyToManyField(to='articleScraper.Journalist')),
            ],
        ),
    ]

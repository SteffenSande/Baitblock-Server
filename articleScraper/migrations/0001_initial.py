# Generated by Django 2.1.4 on 2019-07-26 17:37

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
                ('modified', models.DateTimeField(null=True, verbose_name='time Of Edit')),
                ('headline', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='headlineScraper.Headline')),
            ],
            options={
                'ordering': ('-headline',),
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
                ('search_for', models.CharField(default='p', max_length=255)),
                ('published', models.CharField(max_length=255)),
                ('updated', models.CharField(max_length=255)),
                ('datetime_attribute', models.CharField(blank=True, max_length=255)),
                ('timezone', models.CharField(default='Europe/Oslo', max_length=255)),
                ('image_attribute', models.CharField(default='src', max_length=255)),
                ('image_text', models.CharField(max_length=255)),
                ('image_photographer', models.CharField(blank=True, max_length=255)),
                ('image_element', models.CharField(max_length=255)),
                ('photographer_delimiter', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), blank=True, default=list, size=None)),
                ('photograph_ignore_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), blank=True, default=list, size=None)),
                ('ignore_content_tag', models.CharField(blank=True, max_length=255)),
                ('subscription', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUrlTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_position', models.IntegerField()),
                ('id_separator', models.CharField(blank=True, max_length=1)),
                ('id_length', models.IntegerField()),
                ('id_type', models.CharField(choices=[('ALPHA_NUMERIC', 'AlphaNumeric'), ('NUMBERS_ONLY', 'Numbers only'), ('LETTERS_ONLY', 'Letters only'), ('OTHER', 'Other')], max_length=255)),
                ('placement', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['placement'],
            },
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default=None, null=True)),
                ('type_of_change', models.IntegerField(default=None, null=True)),
                ('pos', models.IntegerField(default=None, null=True)),
            ],
            options={
                'ordering': ('pos',),
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.IntegerField(default=-1)),
            ],
            options={
                'ordering': ('content',),
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField(default=-1)),
                ('tag', models.TextField(default=None, null=True)),
                ('content', models.TextField(default=None, null=True)),
            ],
            options={
                'ordering': ('pos',),
            },
        ),
        migrations.CreateModel(
            name='Diff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('id',),
            },
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
                ('timestamp', models.DateTimeField(null=True, verbose_name='time of revision')),
                ('version', models.IntegerField(verbose_name='version number')),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
                ('words', models.IntegerField()),
                ('subscription', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleScraper.Article')),
                ('images', models.ManyToManyField(to='articleScraper.ArticleImage')),
                ('journalists', models.ManyToManyField(to='articleScraper.Journalist')),
            ],
            options={
                'ordering': ('version',),
            },
        ),
    ]

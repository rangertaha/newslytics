# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-26 03:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import fontawesome.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=100)),
                ('middle', models.CharField(blank=True, max_length=100)),
                ('last', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('sentiment', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='filer.Image')),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('type', models.CharField(blank=True, choices=[('save', 'Save'), ('update', 'Update')], max_length=5, null=True)),
                ('url', models.URLField(blank=True, max_length=250)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='people.Person')),
            ],
            options={
                'verbose_name_plural': 'Social Accounts',
            },
        ),
    ]

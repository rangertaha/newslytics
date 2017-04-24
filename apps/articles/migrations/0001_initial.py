# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-24 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        ('people', '0001_initial'),
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250)),
                ('url', models.URLField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('html', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('image', models.URLField(blank=True, max_length=500, null=True)),
                ('authors', models.ManyToManyField(related_name='articles', to='people.Person')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='domains.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30)),
                ('freq', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(to='articles.Keyword'),
        ),
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Language'),
        ),
        migrations.AddField(
            model_name='article',
            name='places',
            field=models.ManyToManyField(related_name='articles', to='places.Place'),
        ),
    ]

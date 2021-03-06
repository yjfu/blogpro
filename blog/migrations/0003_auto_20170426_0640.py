# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170410_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('excerpt', models.CharField(blank=True, max_length=200)),
                ('author', models.CharField(blank=True, max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('url', models.URLField(blank=True)),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
        migrations.RemoveField(
            model_name='artical',
            name='author',
        ),
        migrations.RemoveField(
            model_name='artical',
            name='category',
        ),
        migrations.RemoveField(
            model_name='artical',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Artical',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-18 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_blog', '0002_blogimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
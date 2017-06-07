# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 16:32
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20170603_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='eeee', editable=False, populate_from='id', unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
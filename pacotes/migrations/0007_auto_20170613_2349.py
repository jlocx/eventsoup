# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 02:49
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0006_auto_20170606_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempacote',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='id', unique=True, verbose_name='Slug'),
        ),
    ]
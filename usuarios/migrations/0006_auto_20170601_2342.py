# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_endereco_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.CharField(default='oi', max_length=20, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=100, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=15, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(max_length=10, verbose_name='Número'),
        ),
    ]
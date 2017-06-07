# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_evento_criador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=250, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('cep', models.CharField(max_length=15, verbose_name='CEP')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.RemoveField(
            model_name='evento',
            name='local',
        ),
        migrations.AddField(
            model_name='endereco',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='evento.Evento', verbose_name='Local do evento'),
        ),
    ]
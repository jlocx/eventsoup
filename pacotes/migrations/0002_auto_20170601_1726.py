# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 17:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacote',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacotes', to=settings.AUTH_USER_MODEL, verbose_name='Dono do Pacote'),
        ),
        migrations.AddField(
            model_name='itempacote',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_pacote', to='pacotes.Item', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='itempacote',
            name='pacote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='pacotes.Pacote', verbose_name='Pacote do Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='criador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to=settings.AUTH_USER_MODEL, verbose_name='Criador do Item'),
        ),
    ]

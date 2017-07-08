# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 18:43
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0013_remove_pacote_codigo_pag_seguro'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='categorias',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('expresso', 'Expresso'), ('casual', 'Casual'), ('festa', 'Festa')], default='q', max_length=21),
            preserve_default=False,
        ),
    ]

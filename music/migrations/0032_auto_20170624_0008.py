# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0031_auto_20170623_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='oglas',
            name='cena',
            field=models.IntegerField(default=100, max_length=30),
        ),
        migrations.AddField(
            model_name='oglas',
            name='grad',
            field=models.CharField(default='Sarajevo', max_length=50),
        ),
    ]

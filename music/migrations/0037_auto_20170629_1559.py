# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0036_employee_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slika',
            field=models.FileField(default='defprofilepic.png', upload_to=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0003_auto_20160329_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='matricula',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]

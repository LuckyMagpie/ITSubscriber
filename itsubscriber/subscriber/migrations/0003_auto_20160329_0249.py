# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0002_auto_20160328_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='id',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='matricula',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

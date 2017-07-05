# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 09:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_auto_20170617_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='numpages',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(50)]),
        ),
    ]
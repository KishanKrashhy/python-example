# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_imagestable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagestable',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp.Student'),
        ),
    ]

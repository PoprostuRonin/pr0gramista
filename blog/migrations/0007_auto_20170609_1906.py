# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170609_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Ikona'),
        ),
    ]
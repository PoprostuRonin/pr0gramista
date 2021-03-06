# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170606_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='compiled_content',
            field=models.TextField(default='', verbose_name='Zawartość skompilowana'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Zawartość'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Tytuł'),
        ),
    ]

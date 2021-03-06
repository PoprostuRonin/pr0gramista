# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-24 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170624_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/posts', verbose_name='Obrazek')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_origin',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='blog.HeaderImage', verbose_name='Główny obrazek'),
            preserve_default=False,
        ),
    ]

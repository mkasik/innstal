# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innstal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]

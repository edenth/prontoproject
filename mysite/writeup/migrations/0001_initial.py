# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.CharField(max_length=200)),
                ('stage', models.IntegerField()),
                ('is_check', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writeup.Report'),
        ),
    ]

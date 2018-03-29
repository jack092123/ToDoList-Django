# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('status', models.TextField(default='unfinished')),
                ('priority', models.TextField(default='low')),
                ('due_date', models.DateField()),
                ('note', models.TextField(blank=True)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'TodoList',
            },
        ),
    ]

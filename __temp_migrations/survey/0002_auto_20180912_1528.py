# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-12 11:28
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='age',
        ),
        migrations.RemoveField(
            model_name='player',
            name='crt_bat',
        ),
        migrations.RemoveField(
            model_name='player',
            name='crt_lake',
        ),
        migrations.RemoveField(
            model_name='player',
            name='crt_widget',
        ),
        migrations.RemoveField(
            model_name='player',
            name='gender',
        ),
        migrations.AddField(
            model_name='player',
            name='major',
            field=otree.db.models.StringField(choices=[('Science, technology, engineering and mathematics', 'Science, technology, engineering and mathematics'), ('Social sciences', 'Social sciences'), ('Art and humanities', 'Art and humanities')], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='sex',
            field=otree.db.models.StringField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10000, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-25 05:37
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('mpl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='choice_1',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_10',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_2',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_3',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_4',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_5',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_6',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_7',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_8',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='choice_9',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-14 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_case_sittings_law_cases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case_sittings',
            name='attend_lawyer',
        ),
        migrations.RemoveField(
            model_name='case_sittings',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='adversary',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='adversay_represent',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='case_category',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='case_classification',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='case_court',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='case_current_status',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='case_depart',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='case_depart_type',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='comapny_represent',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='current_lawyer',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='degree_of_litigation',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='law_cases',
            name='weighted_percent_of_gain',
        ),
        migrations.DeleteModel(
            name='case_sittings',
        ),
        migrations.DeleteModel(
            name='law_cases',
        ),
    ]

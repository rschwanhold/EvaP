# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0046_delete_old_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degrees',
            field=models.ManyToManyField(related_name='courses', to='evaluation.Degree', verbose_name='degrees'),
        ),
    ]

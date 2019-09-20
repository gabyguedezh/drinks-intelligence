# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-14 18:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_auto_20190914_1903'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='piece',
            unique_together=set([('requested_by', 'subject', 'piece_type')]),
        ),
    ]

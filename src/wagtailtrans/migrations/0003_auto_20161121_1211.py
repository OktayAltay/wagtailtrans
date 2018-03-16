# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 12:11
from django.db import migrations, models
import django.db.models.deletion
import wagtailtrans.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailtrans', '0002_auto_20161106_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatablepage',
            name='language',
            field=models.ForeignKey(default=wagtailtrans.models._language_default, on_delete=django.db.models.deletion.PROTECT, related_name='pages', to='wagtailtrans.Language'),
        ),
    ]

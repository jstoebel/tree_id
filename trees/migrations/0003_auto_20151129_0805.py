# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
# renames text to guess and adds a question column.

class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20151128_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='text',
            new_name='guess',
        ),
        migrations.AddField(
            model_name='node',
            name='question',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

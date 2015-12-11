# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0003_auto_20151129_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='edge',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

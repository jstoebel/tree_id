# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

#allows null values in parent column
class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='parent',
            field=models.ForeignKey(to='trees.Node', null=True),
        ),
    ]

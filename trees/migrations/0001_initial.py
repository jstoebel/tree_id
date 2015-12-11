# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

#intial migration of the database
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('edge', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='trees.Node')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('Duration', models.CharField(max_length=200)),
                ('Venue', models.CharField(max_length=200)),
            ],
        ),
    ]

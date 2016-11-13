# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=b'20', verbose_name=b'Name product')),
                ('description', models.TextField()),
                ('quality', models.IntegerField()),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'ordering': ['-quality', 'name'],
            },
        ),
    ]

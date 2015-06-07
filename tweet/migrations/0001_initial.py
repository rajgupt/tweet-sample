# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='handle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=256)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('author', models.ForeignKey(to='tweet.handle')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.SmallIntegerField()),
                ('number', models.SmallIntegerField()),
                ('airdate', models.DateField()),
                ('airstamp', models.DateTimeField()),
                ('runtime', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type_s', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(related_name='episodes', to='tvshows.Show'),
        ),
    ]

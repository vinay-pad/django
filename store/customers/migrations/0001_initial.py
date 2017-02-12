# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('zipCode', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colorName', models.CharField(max_length=50)),
                ('hexValue', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerId', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('customerName', models.CharField(max_length=200)),
                ('customerAddress', models.ForeignKey(related_name='customers', to='customers.Address')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(related_name='segments', to='customers.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('segment', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customersegment',
            name='segment',
            field=models.ForeignKey(related_name='customers', to='customers.Segment'),
        ),
    ]

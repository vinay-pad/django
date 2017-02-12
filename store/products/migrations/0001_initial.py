# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productId', models.CharField(max_length=20)),
                ('productName', models.CharField(max_length=100)),
                ('productCategory', models.ForeignKey(related_name='products', to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subCategory', models.CharField(max_length=50)),
                ('category', models.ForeignKey(related_name='sub_categories', to='products.Category')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='productSubCategory',
            field=models.ForeignKey(related_name='products', to='products.SubCategory'),
        ),
    ]

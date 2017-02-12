# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Colors',
        ),
        migrations.AlterUniqueTogether(
            name='customersegment',
            unique_together=set([('customer', 'segment')]),
        ),
    ]

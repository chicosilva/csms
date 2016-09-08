# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0014_auto_20150604_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='recarga_id',
            field=models.IntegerField(null=True, verbose_name='Regarga Id', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0008_recarga_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='valorrecarga',
            name='descricao',
            field=models.CharField(default=datetime.datetime(2015, 5, 28, 22, 29, 44, 181509, tzinfo=utc), max_length=40, verbose_name='Descri\xe7\xe3o'),
            preserve_default=False,
        ),
    ]

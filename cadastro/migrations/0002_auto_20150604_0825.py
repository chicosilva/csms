# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 11, 25, 27, 857731, tzinfo=utc), verbose_name='Cadastro'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 11, 25, 27, 857731, tzinfo=utc), verbose_name='Cadastro'),
        ),
    ]

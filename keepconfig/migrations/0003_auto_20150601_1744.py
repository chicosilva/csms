# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keepconfig', '0002_auto_20150529_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=15, null=True, verbose_name='Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=250, null=True, verbose_name='Endere\xe7o', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=15, null=True, verbose_name='N\xfamero', blank=True),
        ),
    ]

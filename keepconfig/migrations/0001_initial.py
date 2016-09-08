# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeepConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo?')),
                ('codigo_cliente', models.IntegerField(verbose_name='C\xf3digo do Cliente')),
                ('valor_sms', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'Keep Config',
                'verbose_name_plural': 'Configs',
            },
        ),
    ]

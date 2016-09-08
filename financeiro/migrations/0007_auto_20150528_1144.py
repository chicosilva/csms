# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0006_recarga_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusPagamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=40, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Status Pagamanto',
                'verbose_name_plural': 'Status Pagamanto',
            },
        ),
        migrations.RemoveField(
            model_name='recarga',
            name='status',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValorRecarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('valor', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
            ],
            options={
                'ordering': ['valor'],
                'verbose_name_plural': 'Valor',
            },
        ),
        migrations.RemoveField(
            model_name='recarga',
            name='valor',
        ),
    ]

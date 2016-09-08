# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20150604_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operadora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True)),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Operadora',
                'verbose_name_plural': 'Operadoras',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='operadora',
            field=models.ForeignKey(verbose_name='Operadora', blank=True, to='cadastro.Operadora', null=True),
        ),
    ]

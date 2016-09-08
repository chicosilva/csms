# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0010_remove_valorrecarga_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=300, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Transacao',
                'verbose_name_plural': 'Transacao',
            },
        ),
    ]

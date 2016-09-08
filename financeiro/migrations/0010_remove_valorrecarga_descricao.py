# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0009_valorrecarga_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valorrecarga',
            name='descricao',
        ),
    ]

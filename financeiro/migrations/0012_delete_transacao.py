# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0011_transacao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transacao',
        ),
    ]

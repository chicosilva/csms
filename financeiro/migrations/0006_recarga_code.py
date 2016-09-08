# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0005_remove_recarga_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='code',
            field=models.CharField(verbose_name='Code', max_length=555, null=True, editable=False, blank=True),
        ),
    ]

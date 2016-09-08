# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0002_remove_mensagem_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 20, 34, 13, 516070, tzinfo=utc), verbose_name='Data de envio', auto_now_add=True),
            preserve_default=False,
        ),
    ]

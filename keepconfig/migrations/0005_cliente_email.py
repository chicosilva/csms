# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('keepconfig', '0004_auto_20150604_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 6, 7, 13, 10, 23, 627824, tzinfo=utc), unique=True, max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]

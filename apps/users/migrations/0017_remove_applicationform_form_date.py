# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180802_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationform',
            name='form_date',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180726_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationform',
            name='gender',
            field=models.CharField(default=b'', max_length=30, verbose_name='Gender'),
        ),
    ]

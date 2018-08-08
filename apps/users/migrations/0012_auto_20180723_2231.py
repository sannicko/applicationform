# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180723_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='state',
            field=models.CharField(max_length=100, verbose_name='State', blank=True),
        ),
    ]

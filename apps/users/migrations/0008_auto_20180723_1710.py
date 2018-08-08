# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180723_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='form_date',
            field=models.DateField(max_length=100, verbose_name='Form Date', blank=True),
        ),
    ]

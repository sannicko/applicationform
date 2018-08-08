# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20180729_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='agreement_signed_date',
            field=models.DateField(auto_now=True, verbose_name='Agreement Signed Date', auto_created=True),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='form_date',
            field=models.DateField(max_length=100, verbose_name='Form Date'),
        ),
    ]

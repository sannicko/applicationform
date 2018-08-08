# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180720_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationuser',
            name='agreement_signed_date',
            field=models.DateField(max_length=100, verbose_name='Agreement Signed Date'),
        ),
    ]

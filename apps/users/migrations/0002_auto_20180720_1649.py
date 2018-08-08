# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationuser',
            name='agreement_signed_date',
            field=models.DateField(max_length=100, null=True, verbose_name='Agreement Signed Date'),
        ),
    ]

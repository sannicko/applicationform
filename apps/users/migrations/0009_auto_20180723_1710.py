# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180723_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='dateOFBirth',
            field=models.DateField(max_length=100, null=True, verbose_name='Date OF Birth'),
        ),
    ]

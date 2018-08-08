# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180720_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationuser',
            name='postCode',
            field=models.IntegerField(max_length=5, null=True, verbose_name=b'Post code / Zip code'),
        ),
    ]

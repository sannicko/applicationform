# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_applicationform_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='agreement_signed_date',
            field=models.DateField(verbose_name='Agreement Signed Date', auto_created=True),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='gender',
            field=models.CharField(max_length=30, verbose_name='Gender', choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180723_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='Martial_status',
            field=models.CharField(max_length=1, verbose_name='Martial Status', choices=[(b'M', b'Married'), (b'S', b'Single')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='allowed_in_usa',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='compensation_claim',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='convicted_or_not',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='domicile_address',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='law_suite',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='other_city',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='work_eligible_usa',
            field=models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180723_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='ceiling_mechanic',
            field=models.BooleanField(verbose_name='Ceiling Mechanic'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='concrete_finisher',
            field=models.BooleanField(verbose_name='Concrete Finisher'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='concrete_forming',
            field=models.BooleanField(verbose_name='Concrete Forming'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='drywall_finisher',
            field=models.BooleanField(verbose_name='DryWall Finisher'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='drywall_hanger',
            field=models.BooleanField(verbose_name='DryWall Hanger'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='framing_mechanic',
            field=models.BooleanField(verbose_name='Framing Mechanic'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='general_larborer',
            field=models.BooleanField(verbose_name='General Larborer'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='masonry_blocklayer',
            field=models.BooleanField(verbose_name='Masonry BlockLayer'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='masonry_bricklayer',
            field=models.BooleanField(verbose_name='Masonry BrickLayer'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='osha_manager',
            field=models.BooleanField(verbose_name='Osha Manager'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='painter_tradesman',
            field=models.BooleanField(verbose_name='Painter Tradesman'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='plaster_tradesman',
            field=models.BooleanField(verbose_name='Plaster Tradesman'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='project_manager',
            field=models.BooleanField(verbose_name='Project Manager'),
        ),
    ]

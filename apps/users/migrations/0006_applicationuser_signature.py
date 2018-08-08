# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_applicationuser_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationuser',
            name='signature',
            field=models.ImageField(default=b'Upload_documents/blank.jpg', null=True, upload_to=b'Upload_documents/'),
        ),
    ]

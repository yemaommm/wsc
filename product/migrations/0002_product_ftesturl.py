# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ftestUrl',
            field=models.URLField(max_length=255, null=True, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95url\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_ftesturl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ftestUrl',
        ),
        migrations.AddField(
            model_name='product',
            name='fparams',
            field=models.CharField(max_length=2000, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xb1\x9e\xe6\x80\xa7', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='fproductName',
            field=models.CharField(max_length=255, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d'),
        ),
    ]

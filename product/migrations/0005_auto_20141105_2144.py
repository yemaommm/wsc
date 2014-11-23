# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20141017_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='fbindtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\xbb\x91\xe5\xae\x9a\xe6\x97\xb6\xe9\x97\xb4', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='qrcode',
            name='fnumber',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='fproductName',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='fremark3',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9f\xa5\xe8\xaf\xa2\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
    ]

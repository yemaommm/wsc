# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20141016_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='fremakr5',
            new_name='fisoNo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='freamrk1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fremark2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fremark3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fremark4',
        ),
    ]

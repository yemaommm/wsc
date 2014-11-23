# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fcorpName', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d', blank=True)),
                ('faddress', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('fcontact', models.CharField(max_length=255, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f', blank=True)),
                ('fchargeMan', models.CharField(max_length=255, null=True, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba', blank=True)),
                ('fmanPicUrl', models.ImageField(max_length=255, upload_to=b'upload/middle', null=True, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('fcorpPicUrl', models.ImageField(max_length=255, upload_to=b'upload/middle', null=True, verbose_name=b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x89\xa7\xe7\x85\xa7\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('ffilePicUrls', models.ImageField(max_length=1000, upload_to=b'upload/middle', null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe8\xb5\x84\xe6\x96\x99', blank=True)),
                ('fdatetime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('fupdatetime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe6\x96\xb0\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('fuserId', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\x94\xa8\xe6\x88\xb7', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a',
                'verbose_name_plural': '\u4f01\u4e1a\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fproductName', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d', blank=True)),
                ('freamrk1', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xae\xb9\xe9\x87\x8f', blank=True)),
                ('fremark2', models.CharField(max_length=255, null=True, verbose_name=b'\xe9\x87\x8d\xe9\x87\x8f', blank=True)),
                ('fremark3', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xbd\x93\xe7\xa7\xaf', blank=True)),
                ('fremark4', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x9d\x90\xe8\xb4\xa8', blank=True)),
                ('fremakr5', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9b\xbd\xe5\xae\xb6\xe6\x8e\x88\xe6\x9d\x83\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('fsmallPicUrl', models.ImageField(max_length=255, upload_to=b'upload/small', null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xb0\x8f\xe5\x9b\xbe', blank=True)),
                ('fpicUrl', models.ImageField(max_length=255, upload_to=b'upload/large', null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xa4\xa7\xe5\x9b\xbe', blank=True)),
                ('fbuyUrl', models.CharField(max_length=255, null=True, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe6\x8c\x89\xe9\x92\xae\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('fshopUrl', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x95\x86\xe5\x9f\x8e\xe6\x8c\x89\xe9\x92\xae\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('fmanualUrl', models.CharField(max_length=255, null=True, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e\xe4\xb9\xa6\xe6\x8c\x89\xe9\x92\xae\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('fdatetime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('fupdatetime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe6\x96\xb0\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('fcorp', models.ForeignKey(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a', to='product.Corp')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fqrcode', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('fdate', models.CharField(max_length=255, null=True, verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('fvolumeNo', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8d\xb7\xe6\xa0\x87\xe5\x8f\xb7', blank=True)),
                ('fisBan', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xa6\x81\xe6\xad\xa2')),
                ('fremark1', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x9f\xa5\xe8\xaf\xa2\xe6\xac\xa1\xe6\x95\xb0', blank=True)),
                ('fremark2', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x9f\xa5\xe8\xaf\xa2\xe5\x9c\xb0\xe7\x82\xb9', blank=True)),
                ('fremark3', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x9f\xa5\xe8\xaf\xa2\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('fproduct', models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81', blank=True, to='product.Product', null=True)),
            ],
            options={
                'verbose_name': '\u4e8c\u7ef4\u7801',
                'verbose_name_plural': '\u4e8c\u7ef4\u7801\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
    ]

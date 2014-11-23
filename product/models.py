# -*- coding: UTF-8 -*-

from django.db import models as m
from django.utils.html import format_html
from django.contrib.auth.models import User
# Create your models here.
UPLOAD_ROOT = 'upload'
LARGE_ROOT = 'upload/large'
MIDDLE_ROOT = 'upload/middle'
SMALL_ROOT = 'upload/small'

class Corp(m.Model):
    fcorpName = m.CharField(max_length=255, blank=True, null=True, verbose_name='企业名')
    faddress = m.CharField(max_length=255, blank=True, null=True, verbose_name='企业地址')
    fcontact = m.CharField(max_length=255, blank=True, null=True, verbose_name='联系方式')
    fchargeMan = m.CharField(max_length=255, blank=True, null=True, verbose_name='负责人')
    fmanPicUrl = m.ImageField(max_length=255, upload_to=MIDDLE_ROOT, blank=True, null=True, verbose_name='负责人图片地址')
    fcorpPicUrl = m.ImageField(max_length=255, upload_to=MIDDLE_ROOT, blank=True, null=True, verbose_name='营业执照图片地址')
    ffilePicUrls = m.ImageField(max_length=1000, upload_to=MIDDLE_ROOT, blank=True, null=True, verbose_name='授权资料')
    fuserId = m.ForeignKey(User, verbose_name='所属用户', blank=True, null=True)
    fdatetime = m.DateTimeField(auto_now_add=True,blank=True, null=True, verbose_name='新增时间')
    fupdatetime = m.DateTimeField(auto_now=True,blank=True, null=True, verbose_name='最新更新时间')


    def __unicode__(self):
        return '%s' % (self.fcorpName,)
    class Meta:
        verbose_name = '企业'
        verbose_name_plural = '企业管理'

class Product(m.Model):
    fproductName = m.CharField(max_length=255, blank=True, null=True, verbose_name='产品名')
    fcorp = m.ForeignKey('Corp', verbose_name='企业')
    fisoNo = m.CharField(max_length=255, blank=True, null=True, verbose_name='产品国家授权编号')
    fsmallPicUrl = m.ImageField(max_length=255, upload_to=SMALL_ROOT, blank=True, null=True, verbose_name='产品小图')
    fpicUrl = m.ImageField(max_length=255, upload_to=LARGE_ROOT, blank=True, null=True, verbose_name='产品大图')
    fbuyUrl = m.CharField(max_length=255,blank=True, null=True, verbose_name='购买按钮地址')
    fshopUrl = m.CharField(max_length=255,blank=True, null=True, verbose_name='商城按钮地址')
    fmanualUrl = m.CharField(max_length=255,blank=True, null=True, verbose_name='说明书按钮地址')
    fdatetime = m.DateTimeField(auto_now_add=True,blank=True, null=True, verbose_name='新增时间')
    fupdatetime = m.DateTimeField(auto_now=True,blank=True, null=True, verbose_name='最新更新时间')
    fparams = m.CharField(max_length=2000, blank=True, null=True, verbose_name='产品属性')


    def __unicode__(self):
        return '%s' % (self.fproductName,)
    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品管理'

class Qrcode(m.Model):
    fqrcode = m.CharField(max_length=255, blank=True, null=True, verbose_name='二维码编号')
    fproduct = m.ForeignKey('Product',blank=True, null=True, verbose_name='产品')
    fdate = m.CharField(max_length=255, blank=True, null=True, verbose_name='生产日期')
    fvolumeNo = m.CharField(max_length=255, blank=True, null=True, verbose_name='卷标号')
    fisBan = m.BooleanField(default=False, verbose_name='是否禁止')
    fremark1 = m.CharField(max_length=255, blank=True, null=True, verbose_name='查询次数')
    fremark2 = m.CharField(max_length=255, blank=True, null=True, verbose_name='查询地点')
    #fremark3 = m.CharField(max_length=255, blank=True, null=True, verbose_name='查询时间')
    fremark3 = m.DateTimeField(blank=True, null=True, verbose_name='查询时间', auto_now=True)
    #add 20141105 
    fnumber = m.CharField(max_length=255, blank=True, null=True, verbose_name='编号')
    fbindtime = m.DateTimeField(blank=True, null=True, verbose_name='绑定时间', auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.fqrcode,)
    class Meta:
        verbose_name = '二维码'
        verbose_name_plural = '二维码管理'


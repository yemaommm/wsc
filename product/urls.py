#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-09-18 23:04:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from product import views

urlpatterns = patterns('',
    url(r'^admin/update/$', views.UpdQrcode.as_view()),
    # url(r'^admin/update/$', views.updateQrcode),
    url(r'^admin/getproduct/$', views.AjaxGetProduct.as_view()),
    # url(r'^admin/getproduct/$', views.ajaxGetProduct),
    url(r'^(.+)/$', views.showInfo),
)

# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, render_to_response,redirect
from django.template.context import RequestContext
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import Corp, Product, Qrcode
from datetime import datetime
from base import BaseView
import json
import logging

# Create your views here.

def showInfo(request, param1):
    qrcode  = None
    product = None
    corp = None
    properties = None
    try:
        qrcode = Qrcode.objects.get(fqrcode=param1)

        try:
            product = Product.objects.get(id=qrcode.fproduct_id)
            if product.fparams:
                properties = json.loads(product.fparams)
            corp = Corp.objects.get(id=product.fcorp_id)
        except Exception, e:
            print e

        queryCount = 0
        try:
            queryCount = int(qrcode.fremark1)
        except Exception, e:
            queryCount = 0
        qrcode.fremark1 = queryCount + 1
        qrcode.fremark2 = '上海'
        #qrcode.fremark3 = datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        qrcode.save()
    except Exception, e:
        print e
    rightnow = datetime.now()
    return render(request, 'product/index.html'
                  , {'product':product, 'corp':corp, 'qrcode':qrcode
                     ,'rightnow':rightnow, 'params':properties},context_instance=RequestContext(request))

class UpdQrcode(BaseView):
    '''批量更新二维码产品信息
    '''
    @method_decorator(login_required(login_url='/admin/login/'))
    def post(self, request, *args, **kwargs):
        productId = request.POST['fproduct']
        qrcodes = request.POST['qrcodes']

        # 自动关闭connection，批量更新 使用 where in 方法
        if productId != '' and qrcodes != '':
            a = tuple([qrcode for qrcode in qrcodes.split(',')])
            with connection.cursor() as c:
                c.execute('UPDATE product_qrcode SET fproduct_id = %s WHERE id IN %s', [productId, a])
            return self.http_redirect('/admin/product/qrcode/?fproduct__id__exact=%s' % productId)
        return self.http_redirect('/admin/product/qrcode/')

class AjaxGetProduct(BaseView):
    # @login_required(login_url='/admin/login/')
    @method_decorator(login_required(login_url='/admin/login/'))
    def get(self, request, *args, **kwargs):
        corpId = 0
        products = []
        if 'corpId' in request.GET:
            corpId = request.GET['corpId']
            try:
                product = Product.objects.filter(fcorp=corpId)
                for p in product:
                    dictP = {'pid':p.id,'pname':p.fproductName}
                    products.append(dictP)
                return HttpResponse(json.dumps(products))
            except Exception, e:
                print e
            return HttpResponse(json.dumps({}))
        return HttpResponse(json.dumps({}))

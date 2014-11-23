# -*- coding: UTF-8 -*-
from django.contrib import admin
from product import models
# from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
# Register your models here.

class CorpAdmin(admin.ModelAdmin):
    list_display = ('fcorpName', 'faddress', 'fcontact', 'fchargeMan', 'fmanPicUrl', 'fcorpPicUrl', 'ffilePicUrls', 'fdatetime', 'fupdatetime')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('fproductName', 'fcorp', 'fisoNo', 'fsmallPicUrl', 'fpicUrl', 'fbuyUrl', 'fshopUrl', 'fmanualUrl', 'fdatetime', 'fupdatetime')

class QrcodeAdmin(admin.ModelAdmin):
    list_display = ( 'fqrcode', 'fproduct', 'fdate', 'fvolumeNo', 'fisBan', 'fremark1', 'fremark2', 'fremark3','fnumber', 'fbindtime')

    list_per_page = 1000

    list_filter = ('fproduct',)

    actions = ['update_product']

    def update_product(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        qrcodes = []
        for i in selected:
            qrcodes.append(i)
        qrcode = ",".join(qrcodes)
        corp = models.Corp.objects.all()
        return render_to_response('product/update_info.html', {'corp':corp, 'qrcodes':qrcode}, context_instance=RequestContext(request))


    update_product.short_description = "批量绑定产品"


admin.site.register(models.Corp,CorpAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Qrcode, QrcodeAdmin)
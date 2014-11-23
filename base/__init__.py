# -*- coding: utf-8 -*-
# @Date    : 2014-10-14 17:10:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from django.http import HttpResponse
from django.shortcuts import render, render_to_response,redirect
from django.views.generic import View
import json

class BaseView(View):
    
    def render_http_success(self, *args, **kwargs):
        pass

    # def render_http_404(self, *args, **kwargs):
    #     pass

    # def render_http_500(self, *args, **kwargs):
    #     pass

    # def render_http_403(self, *args, **kwargs):
    #     pass

    def render_json_success(self, *args, **kwargs):
        return HttpResponse(json.dumps({'a':1}))

    def render_json_failure(self, *args, **kwargs):
        return HttpResponse({})

    def http_redirect(self, url, *args, **kwargs):
        return redirect(url)

    def ajax_redirect(self, url, *args, **kwargs):
        return redirect(url)
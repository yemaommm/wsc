from django.conf.urls import patterns, include, url
from django.contrib import admin
from conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wsc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pr/', include('product.urls',namespace='product')),
    url(r'^upload/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_UPLOAD}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    # (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
#urlpatterns += staticfiles_urlpatterns()

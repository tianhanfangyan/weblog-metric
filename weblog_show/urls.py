#coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('weblog_show.views',
    # url(r"^","weblog_show"),
    url(r"^Home/","Home"),
    url(r"^ip/","ip"),
    url(r"^pv/","pv"),
    url(r"^uv/","uv"),
    url(r"^source/","source"),
    url(r"^device/","device"),
    url(r"^request_getSourceData/","request_getSourceData"),
    url(r"^request_getDeviceData/","request_getDeviceData"),
    url(r"^request_getUVData/","request_getUVData"),
    url(r"^request_getPVData/","request_getPVData"),
    url(r"^request_getIPData/","request_getIPData"),
    
    
    
)


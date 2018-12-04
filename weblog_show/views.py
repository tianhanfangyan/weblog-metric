# -*- coding:utf-8 -*-
import pdb
import optparse
import os
import codecs
import shutil
import sys
import time
import random
import json
import socket
import tarfile
import urllib2
from django.http import HttpResponse
from weblog_base import settings
from weblog_base.utils import render_template,render_json,noc_permission

#插入weblog_show的models
from django.db import models
from weblog_show.models import *

#日志管理
import logging
logger = logging.getLogger('django')
error_logger = logging.getLogger('error')

reload(sys)
sys.setdefaultencoding('utf-8')

#页面加载时就执行
def Home(request):
   return render_template("Home.html",request=request)
def ip(request):
   return render_template("ip.html",request=request)
def uv(request):
   return render_template("uv.html",request=request)
def pv(request):
   return render_template("pv.html",request=request)
def source(request):
   return render_template("source.html",request=request) 
def device(request):
   return render_template("device.html",request=request)      



# 从mysql拉取数据并转化为json
# def request_getAllData(request):
#     response=[]
#     pEquipmentList=WeblogShowTest.objects.all()
#     for equipType in pEquipmentList:
#         subResponse={}
#         subResponse['time']=equipType.time
#         subResponse['num']=equipType.num
#         response.append(subResponse)
#     httpresponse = HttpResponse(json.dumps(response),content_type="application/json")
#     httpresponse['Content-Length']=len(httpresponse.content)  
#     return httpresponse 


def request_getSourceData(request):
    response1=[]
    pEquipmentList1=DmSource.objects.all()
    for equipType1 in pEquipmentList1:
        subResponse1={}
        subResponse1['source']=equipType1.source
        subResponse1['num']=equipType1.num
        response1.append(subResponse1)
    httpresponse = HttpResponse(json.dumps(response1),content_type="application/json")
    httpresponse['Content-Length']=len(httpresponse.content)  
    return httpresponse 

def request_getDeviceData(request):
    response=[]
    pEquipmentList=DmDevice.objects.all()
    for equipType in pEquipmentList:
        subResponse={}
        subResponse['device']=equipType.device
        subResponse['num']=equipType.num
        response.append(subResponse)
    httpresponse = HttpResponse(json.dumps(response),content_type="application/json")
    httpresponse['Content-Length']=len(httpresponse.content)  
    return httpresponse 

def request_getUVData(request):
    response=[]
    pEquipmentList=DmKpiInfo.objects.all()
    for equipType in pEquipmentList:
        subResponse={}
        subResponse['time']=equipType.time
        subResponse['uv']=equipType.uv
        response.append(subResponse)
    httpresponse = HttpResponse(json.dumps(response),content_type="application/json")
    httpresponse['Content-Length']=len(httpresponse.content)  
    return httpresponse 

def request_getPVData(request):
    response=[]
    pEquipmentList=DmKpiInfo.objects.all()
    for equipType in pEquipmentList:
        subResponse={}
        subResponse['time']=equipType.time
        subResponse['pv']=equipType.pv
        response.append(subResponse)
    httpresponse = HttpResponse(json.dumps(response),content_type="application/json")
    httpresponse['Content-Length']=len(httpresponse.content)  
    return httpresponse 

def request_getIPData(request):
    response=[]
    pEquipmentList=DmKpiInfo.objects.all()
    for equipType in pEquipmentList:
        subResponse={}
        subResponse['time']=equipType.time
        subResponse['ip']=equipType.ip
        response.append(subResponse)
    httpresponse = HttpResponse(json.dumps(response),content_type="application/json")
    httpresponse['Content-Length']=len(httpresponse.content)  
    return httpresponse 



   








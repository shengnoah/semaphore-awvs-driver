# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import json
import syslog_client

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def output_graylog(msg):
    graylog = syslog_client.Syslog("127.0.0.1")
    graylog.send(json.dumps(msg), syslog_client.Level.INFO)


def output_graylog_interface(msg):
    import syslog_client_update
    graylog = syslog_client_update.Syslog("127.0.0.1")
    graylog.send(json.dumps(msg), syslog_client.Level.INFO)


def get_phone_num(request, ver):
    return HttpResponse('test',content_type="text/plain")


@csrf_exempt
def XSend(request):
    import requests
    #r = requests.post('http://127.0.0.1/mail/', json.dumps({"message":"测试消息","access_key":""}))

    print request.method
    return HttpResponse('test',content_type="text/plain")

@csrf_exempt
def SendWxMessage(request):
    #print request.method
    if request.method == 'GET':
        return JSONResponse("GET dealChangeStaff")
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        flg_message = data.has_key('message')
        xmessage = data['message']
        access_key = data['access_key']

        if cmp(access_key, "testkey"):
        	return JSONResponse("key")


    return HttpResponse('done',content_type="text/plain")

@csrf_exempt
def dealRouteChange(request):
    print request.method
    if request.method == 'GET':
        return JSONResponse("GET")
    
    if request.method == 'POST':
        data = JSONParser().parse(request)

        flg_source= data.has_key('source')
        flg_domain = data.has_key('domain')
        flg_index = data.has_key('index')
        flg_file = data.has_key('file')
        flg_params = data.has_key('params')
        flg_params = data.has_key('content')

        flg_key = data.has_key('key')
        if not flg_key:            
            return JSONResponse('key is empty!')
        access_key = data['key']

        if cmp(access_key, "test"):
        	return JSONResponse("access key error.")

        flg_source = data.has_key('source')
        if not flg_source:            
            result = {"error":"-1","errmsg":"source is empty"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

        flg_domain = data.has_key('domain')
        if not flg_domain:            
            result = {"error":"-1","errmsg":"domain is empty"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

        flg_index = data.has_key('index')
        if not flg_index:            
            result = {"error":"-1","errmsg":"index is empty"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

        flg_file = data.has_key('file')
        if not flg_file:            
            result = {"error":"-1","errmsg":"file is empty"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

        flg_params = data.has_key('params')
        if not flg_params:            
            result = {"error":"-1","errmsg":"params is empty"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

        flg_content = data.has_key('content')
        if not flg_content:            
            result = {"error":"-1","errmsg":"content is empty"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

        msg = data

        from jsonrpc.proxy import ServiceProxy
        s = ServiceProxy('http://localhost:5000/json/')
        s.myapp.sayHello('Sam')

        result = {"error":"0","errmsg":"none"}
        return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
   

@csrf_exempt
def outputJson(request):
    print request.method
    if request.method == 'GET':
        return JSONResponse("GET")
    
    if request.method == 'POST':
        result = {"error":"0","errmsg":"empty"}
        return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    
    return HttpResponse('test',content_type="text/plain")

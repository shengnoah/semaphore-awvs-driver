# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.



from jsonrpc import jsonrpc_method

@jsonrpc_method('myapp.sayHello')
def whats_the_time(request, name='Lester'):
  import awvs
  ins = awvs.AWVS("test.com")
  ret = ins.send(5) 
  
  return "Hello %s" % ins.domain 

@jsonrpc_method('myapp.gimmeThat', authenticated=True)
def something_special(request, secret_data):
  return {'sauce': ['authenticated', 'sauce']}

@jsonrpc_method('scanner.sayHello')
def whats_the_time(request, name='Lester'):
  return "Scanner %s" % name


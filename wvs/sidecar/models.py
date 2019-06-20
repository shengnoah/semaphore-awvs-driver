# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
# Create your models here.



class testcase(models.Model):
    name1 = models.CharField(max_length=300)
    name2 = models.CharField(max_length=300)
    name3 = models.CharField(max_length=300)
    def __unicode__(self):
        #return self.obj_type 
        #tmp = self.obj_type % self.device_number
        columns = u"%s %s %s" % (self.name1, self.name2, self.name3)
        return columns


class cmdb(models.Model):
    obj_type = models.CharField(max_length=300)
    device_number = models.CharField(max_length=300)
    ip = models.CharField(max_length=300)
    device_status = models.CharField(max_length=300)
    device_mod = models.CharField(max_length=300)
    device_locate = models.CharField(max_length=300)
    admin = models.CharField(max_length=300)
    product_tree = models.CharField(max_length=300)
    isp = models.CharField(max_length=300)
    current_user = models.CharField(max_length=300)
    product = models.CharField(max_length=300)
    upstream_device = models.CharField(max_length=300)
    downstream_device = models.CharField(max_length=300)
    requirement = models.CharField(max_length=300)
    def __unicode__(self):
        #return self.obj_type 
        #tmp = self.obj_type % self.device_number
        columns = u"%s %s %s %s %s %s" % (self.current_user, self.admin, self.obj_type , self.device_number, self.ip, self.device_locate)
        return columns
         
class Admin:
    list_display = ("object_type","device_number","ip","device_status","device_mod","device_locate","admin","product_tree","isp","current_user","product","upstream_device","downstream_device","requirement")


admin.site.register(cmdb)
admin.site.register(testcase)


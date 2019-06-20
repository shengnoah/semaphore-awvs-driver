from django.conf.urls import url
from restapi import views

urlpatterns = [
    url(r'get_phone/(\d{1,6})/$', views.get_phone_num),  
    url(r'mail/$', views.SendWxMessage),          
    url(r'xsend/$', views.XSend),          
    url(r'interface_update/$', views.dealRouteChange),
    url(r'output_json/$', views.outputJson),
]

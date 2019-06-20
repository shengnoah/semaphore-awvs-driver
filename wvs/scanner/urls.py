from django.conf.urls import url
#import jsonrpc
from jsonrpc import jsonrpc_site
from scanner import views


urlpatterns = [ 
  #url(r'^json/browse/', jsonrpc.views.browse), # for the graphical browser/web console only, omissible
  url(r'^json/', jsonrpc_site.dispatch),
  url(r'^json/(?P<method>[a-zA-Z0-9.]+)$',jsonrpc_site.dispatch) # for HTTP GET only, also omissible
]



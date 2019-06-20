from django.conf.urls import url
from sidecar import views

urlpatterns = [
    url(r'sidecar/$', views.sidecar),      
]

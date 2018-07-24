__author__ = "xiaoyu hao"

from django.conf.urls import url,include

from monitor import api_views

urlpatterns = [
    url(r'client/config/(\d+)/$',api_views.client_config),
    url(r'client/service/report/$',api_views.service_report),
]
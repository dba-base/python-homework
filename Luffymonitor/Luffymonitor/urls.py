"""Luffymonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^api/', include("monitor.api_urls")),
    url(r'^monitor/db_list$', views.db_list,name='db_list'),
    url(r'^monitor/tablespace/$', views.tablespace,name='tablespace'),
    url(r'^monitor/items$', views.monitor_items,name='monitor_items'),
    url(r'^report/', views.report, name='report'),
    url(r'^detail/', views.tbs_detail, name='tbs_detail'),
    url(r'^modal/', views.modal, name='modal')
]

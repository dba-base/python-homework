"""AutoOps URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.dashboard),
    url(r'^user_audit/$', views.user_audit,name="user_audit"),
    url(r'^audit_log/(\w+-\w+-\w+)/$', views.audit_log_date,name="audit_log_date"),
    url(r'^audit_log/(\w+-\w+-\w+)/(\d+)/$', views.audit_log_detail,name="audit_log_detail"),
    url(r'^webssh/$', views.webssh,name="webssh"),
    url(r'^multitask/cmd/$', views.multitask_cmd,name="multitask_cmd"),
    url(r'^multitask/file_transfer/$', views.multitask_file_transfer,name="multitask_file_transfer"),
    url(r'^multitask/$', views.multitask,name="multitask"),
    url(r'^multitask/result/$', views.multitask_result,name="task_result"),



    url(r'^login/$', views.acc_login),
    url(r'^logout/$', views.acc_logout,name="logout"),

]

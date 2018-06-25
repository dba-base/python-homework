from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from web.views import account
from web.views import home
from web.views import asset

urlpatterns = [
    url(r'^login.html$', account.LoginView.as_view()),
    url(r'^logout.html$', account.LogoutView.as_view()),
    url(r'^index.html$', home.IndexView.as_view()),
    url(r'^cmdb.html$', home.CmdbView.as_view()),
    url(r'^asset.html$', asset.AssetView.as_view()),
    url(r'^assets.html$', asset.AssetsView.as_view()),
    url(r'^chart-(?P<chart_type>\w+).html$', home.ChartView.as_view()),
]

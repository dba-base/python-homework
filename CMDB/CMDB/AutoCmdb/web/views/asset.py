#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from web.service import asset


class AssetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'asset.html')


class AssetsView(View):
    def get(self, request):
        response = asset.Asset.fetch_assets(request)
        return JsonResponse(response.__dict__)

    def delete(self, request):
        response = asset.Asset.delete_assets(request)
        return JsonResponse(response.__dict__)

    def put(self,request):
        response = asset.Asset.put_assets(request)
        return JsonResponse(response.__dict__)
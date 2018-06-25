#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from django.db.models import Q
from repository import models
from utils.pager import PageInfo
from utils.response import BaseResponse
from django.http.request import QueryDict


class Asset(object):
    @staticmethod
    def assets_condition(request):
        con_str = request.GET.get('condition', None)
        if not con_str:
            con_dict = {}
        else:
            con_dict = json.loads(con_str)

        con_q = Q()
        for k, v in con_dict.items():
            temp = Q()
            temp.connector = 'OR'
            for item in v:
                temp.children.append((k, item))
            con_q.add(temp, 'AND')

        return con_q

    @staticmethod
    def condition_config():
        values = [
            {'name': 'cabinet_num', 'text': '机柜号', 'condition_type': 'input'},
            {'name': 'device_type_id', 'text': '资产类型', 'condition_type': 'select', 'global_name': 'device_type_list'},
            {'name': 'device_status_id', 'text': '资产状态', 'condition_type': 'select', 'global_name': 'device_status_list'},
        ]
        return values

    @staticmethod
    def table_config():
        values = [
            {
                'q': 'id',
                'title': "ID",
                'display': 1,
                'attr': {}
            },
            {
                'q': 'idc_id',
                'title': "IDC",
                'display': 0,
                'attr': {}
            },
            {
                'q': 'idc__name',
                'title': "IDC",
                'display': 1,
                'attr': {'name': 'idc_id', 'id': '@idc_id', 'edit-enable': 'true', 'edit-type': 'select',
                         'global-name': 'idc_list'}
            },
            {
                'q': 'cabinet_num',
                'title': "机柜号",
                'display': 1,
                'attr': {'name': 'cabinet_num', 'edit-enable': 'true', 'edit-type': 'input', }
            },
            {
                'q': 'cabinet_order',
                'title': "位置",
                'display': 1,
                'attr': {'name': 'cabinet_order', 'edit-enable': 'true', 'edit-type': 'input', }
            },
            {
                'q': 'business_unit_id',
                'title': "业务线ID",
                'display': 0,
                'attr': {}
            },
            {
                'q': 'business_unit__name',
                'title': "业务线",
                'display': 1,
                'attr': {'name': 'business_unit_id', 'id': '@business_unit_id', 'edit-enable': 'true',
                         'edit-type': 'select',
                         'global-name': 'business_unit_list'}
            },
            {
                'q': 'device_status_id',
                'title': "资产状态",
                'display': 2,
                'attr': {'name': 'device_status_id', 'id': '@@device_status_list', 'edit-enable': 'true',
                         'edit-type': 'select',
                         'global-name': 'device_status_list'}
            },
            {
                'q': 'device_type_id',
                'title': "资产类型",
                'display': 2,
                'attr': {'name': 'device_type_id', 'id': '@@device_type_list', 'edit-enable': 'true',
                         'edit-type': 'select',
                         'global-name': 'device_type_list'}
            },
        ]
        return values

    @classmethod
    def asset_values(cls):
        values = []
        for item in cls.table_config():
            values.append(item['q'])
        return values

    @staticmethod
    def device_status_list():
        result = map(lambda x: {'id': x[0], 'name': x[1]}, models.Asset.device_status_choices)
        return list(result)

    @staticmethod
    def device_type_list():
        result = map(lambda x: {'id': x[0], 'name': x[1]}, models.Asset.device_type_choices)
        return list(result)

    @staticmethod
    def idc_list():
        values = models.IDC.objects.only('id', 'name', 'floor')
        result = map(lambda x: {'id': x.id, 'name': "%s-%s" % (x.name, x.floor)}, values)
        return list(result)

    @staticmethod
    def business_unit_list():
        values = models.BusinessUnit.objects.values('id', 'name')
        return list(values)

    @classmethod
    def fetch_assets(cls, request):
        response = BaseResponse()
        try:
            ret = {}
            conditions = cls.assets_condition(request)
            asset_count = models.Asset.objects.filter(conditions).count()
            page_info = PageInfo(request.GET.get('pager', None), asset_count)
            asset_list = models.Asset.objects.filter(conditions).values(*cls.asset_values())[
                         page_info.start:page_info.end]

            ret['table_config'] = cls.table_config()
            ret['condition_config'] = cls.condition_config()

            ret['data_list'] = list(asset_list)

            ret['page_info'] = {
                "page_str": page_info.pager(),
                "page_start": page_info.start,
            }

            ret['global_dict'] = {
                'device_status_list': cls.device_status_list(),
                'device_type_list': cls.device_type_list(),
                'idc_list': cls.idc_list(),
                'business_unit_list': cls.business_unit_list()
            }
            response.data = ret
            response.message = '获取成功'
        except Exception as e:
            response.status = False
            response.message = str(e)

        return response

    @classmethod
    def delete_assets(cls, request):
        response = BaseResponse()
        try:
            delete_dict = QueryDict(request.body, encoding='utf-8')
            print(delete_dict)
            id_list = delete_dict.getlist('id_list')
            print(id_list)
            models.Asset.objects.filter(id__in=id_list).delete()
            response.message = '删除成功'
        except Exception as e:
            response.status = False
            response.message = str(e)
        return response

    @classmethod
    def put_assets(cls, request):
        response = BaseResponse()
        try:
            response.error = []
            put_dict = QueryDict(request.body, encoding='utf-8')
            update_list = json.loads(put_dict.get('update_list'))
            error_count = 0
            for row_dict in update_list:
                nid = row_dict.pop('nid')
                num = row_dict.pop('num')
                try:
                    models.Asset.objects.filter(id=nid).update(**row_dict)
                except Exception as e:
                    response.error.append({'num': num, 'message': str(e)})
                    response.status = False
                    error_count += 1
            if error_count:
                response.message = '共%s条,失败%s条' % (len(update_list), error_count,)
            else:
                response.message = '更新成功'
        except Exception as e:
            response.status = False
            response.message = str(e)
        return response




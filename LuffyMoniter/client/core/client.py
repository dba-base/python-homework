#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import time
import hashlib
import requests
from src import plugins
from lib.serialize import Json
from lib.log import Logger
from config import settings

from concurrent.futures import ThreadPoolExecutor


class AutoBase(object):
    def __init__(self):
        self.asset_api = settings.ASSET_API
        self.key = settings.KEY
        self.key_name = settings.AUTH_KEY_NAME

class AutoSSH(AutoBase):
    def process(self):
        """
        根据主机名获取资产信息，将其发送到API
        :return:
        """
        task = self.get_asset()
        if not task['status']:
            Logger().log(task['message'], False)

        pool = ThreadPoolExecutor(10)
        for item in task['data']:
            hostname = item['hostname']
            pool.submit(self.run, hostname)
        pool.shutdown(wait=True)

    def run(self, hostname):
        server_info = plugins.get_server_info(hostname)
        server_json = Json.dumps(server_info.data)
        self.post_asset(server_json, self.callback)

class AutoJDBC():
    def process(self):
        pass




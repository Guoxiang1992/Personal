# -- coding: utf-8 --
# @File : base_page.py
import requests
import yaml


class BasePage:
    def data_driven(self,path):
        with open(path) as f:
            data = yaml.safe_load(f)
            return data
    def req(self,method,url,param=None):
        return requests.request(method=method,url=url,params=param)
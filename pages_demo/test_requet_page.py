# -- coding: utf-8 --
# @File : test_requet_page.py
import requests
from project.lagouPY.requests_demo.request_po_demo.pages_demo.base_page import BasePage

class TestRequestDemo:
    def setup(self):
        self.base = BasePage()
    def test_po_get(self):
        data = self.base.data_driven('../pages_demo/data.yml')
        method = data['request1']['method']
        url = data['request1']['url']
        param = data['request1']['param']
        r=self.base.req(method,url,param)
        print(r.text)

    def test_po_post(self):
        data = self.base.data_driven('../pages_demo/data.yml')
        method = data['request2']['method']
        url = data['request2']['url']
        param = data['request2']['param']
        r = requests.request(method=method, url=url, data=param,headers=param)
        print(r.text)

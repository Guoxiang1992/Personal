# -- coding: utf-8 --
# @File : weather.py
import requests
class Weather:
    def __init__(self):
        self.request=requests.session()
    def get(self,cityid,city,*args,**kwargs):
        url = f'http://www.weather.com.cn/data/cityinfo/{cityid}.html'
        r = self.request.request(method='GET',url=url,*args,**kwargs)
        r.encoding='utf-8'
        print(f"查询城市{city}--查询结果为{r.json()}")
        assert city == r.json()['weatherinfo']['city']
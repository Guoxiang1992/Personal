# -- coding: utf-8 --
# @File : case_weather.py
import allure

from weather.weather_demo.weather import Weather
@allure.feature('Test Weather api')
class TestWeather:
    def setup(self):
        self.weather=Weather()
    @allure.story('查询深圳天气')
    def test_1(self):
        self.weather.get('101280601','深圳')
    @allure.story('查询北京天气')
    def test_2(self):
        self.weather.get('101010100','北京')
    @allure.story('查询上海天气')
    def test_3(self):
        self.weather.get('101020100','上海')
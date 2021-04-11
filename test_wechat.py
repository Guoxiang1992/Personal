# -- coding: utf-8 --
# @File : test_wechat.py
import time

from appium import webdriver


class TestWeChart:
    def setup(self):
        condition = {
            "platformName": "android",
            "deviceName": "111", #一定不能少这个参数
            "udid": "127.0.0.1:7555", #如果只有一个设备可以不写，多个设备就要写进行指定
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "settings[waitForIdleTimeout]": 0, #把动态网页，当作静态处理，减少元素定位时间，一定是[]不能是()
            "noReset": "true",  # 记录之前的操作或登录信息，不清除缓存
            "skipDeviceInitialization": "true"  # 跳过设备初始化
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", condition)  # ip port num不要忘记！！
        self.driver.implicitly_wait(5)

    def test_wechat(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        #这里打卡页面，打卡元素在下面，无法直接定位，只能通过滚动定位
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("打卡").'
                                                        'instance(0));').click()
        self.driver.find_element_by_id('com.tencent.wework:id/i1x').click()
        #文本属性包含外出的进行定位
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("次外出")').click() #注意Contains是大写
        #也可以这么写
        # self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]")
        ele = self.driver.find_element_by_id('com.tencent.wework:id/pu').text
        assert '外出打卡成功' == ele


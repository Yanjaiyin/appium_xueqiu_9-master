# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestxueqiuAPP(object):

    @classmethod
    def init_xueqiu(cls):
        caps = {}

        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["platformVersion"] = "6.0.1"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(30)
        return driver

    @classmethod
    def setup_class(cls):
        print("setup class")
        cls.driver = TestxueqiuAPP.init_xueqiu()
        #click top left button
        cls.driver.find_element_by_id("user_profile_icon").click()
        #veriy 点击登陆 exist
        cls.driver.find_element_by_id("tv_login")


    def setup_method(self):
        print("setup method")
        #click 点击登陆
        self.driver.find_element_by_id("tv_login").click()
        #click 手机及其他登陆
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        #verify 登陆 exist
        self.driver.find_element_by_id("button_next")


    def test_phone(self):
        sNumber = "18140672212"
        sVerifyCode = "1234"
        #click 请输入手机号
        self.driver.find_element_by_id("register_phone_number").send_keys(sNumber)
        self.driver.find_element_by_id("register_code").send_keys(sVerifyCode)
        #click 登陆
        self.driver.find_element_by_id("button_next").click()

        #Verify a alert message pop up
        self.driver.find_element_by_xpath("//*[@resource-id='android:id/content']//*[@text='验证码已过期']")
        #click 确定
        self.driver.find_element_by_xpath("//*[@resource-id='android:id/content']//*[@text='确定']").click()


    def test_phone_and_mail(self):
        #click手机登陆及邮箱
        self.driver.find_element_by_id("tv_login_with_account").click()


    def teardown_method(self):
        self.driver.back()




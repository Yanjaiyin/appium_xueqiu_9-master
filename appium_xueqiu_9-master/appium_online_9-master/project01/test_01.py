# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import time

class TestxueqiuAndroid(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print("set up class")
        cls.driver = cls.init_Appuim()

    def setup_method(self):
        print("set method")
        self.driver = webdriver
        self.driver = TestxueqiuAndroid.driver

    def test_login(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
        el3.click()



    def test_jijin(self):
        self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']").click()

    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']").click()
        for i in range(5):
            self.driver.swipe(300,1000,300,300)
            time.sleep(2)

    def test_action(self):
        self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']").click()
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=300, y=1000).move_to(x=300, y=300).release().perform()
            time.sleep(2)
            self.driver.get_screenshot_as_file(str(i)+'.png')

    def test_action_p(self):
        rect = self.test_window_size()

        self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']").click()
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=rect['width']*0.8, y=rect['height']*0.8)\
                .move_to(x=rect['width']*0.2, y=rect['height']*0.2)\
                .release()\
                .perform()
            time.sleep(2)


    def test_window_size(self):
        rect = self.driver.get_window_size()
        return rect




    def teardown_method(self):
        self.driver.back()


    @classmethod
    def init_Appuim(cls) -> webdriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 追加一句
        driver.implicitly_wait(30)
        return driver






import time
from appium import webdriver


class Testxueqiu_homework2(object):

    def setup_method(self):
        self.driver = self.init_appium()
        print("setup method")


    def test_swipe(self):
        rect = self.driver.get_window_size()
        for j in range(7):
            self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']").click()
            for i in range(5):
                self.driver.swipe(rect['width']*0.8, rect['height']*0.8,rect['width']*0.2, rect['height']*0.2)
                time.sleep(2)
            self.driver.swipe(rect['width'] * 0.8, rect['height'] * 0.5, rect['width'] * 0.2, rect['height'] * 0.5)
            time.sleep(2)

    def init_appium(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["platformVersion"] = "6.0.1"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        # 追加一句
        driver.implicitly_wait(30)
        return driver

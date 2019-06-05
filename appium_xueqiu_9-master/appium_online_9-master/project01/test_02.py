from appium import webdriver
from appium.webdriver import webdriver
from appium.webdriver.webdriver import WebDriver

class TestAppuimAPI(object):


    def setup_method(self):
        self.driver = self.init_Appium()
        print("Setup method : 执行所有测试用例之前只执行一次")

    def test_api(self):
        rect = self.driver.get_window_rect()
        print(rect['width'])

        print(self.driver.get_window_size())
        print(self.driver.mobile)


    def teardown_method(self):
        self.driver.quit()


    def init_Appium(self) ->WebDriver:
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


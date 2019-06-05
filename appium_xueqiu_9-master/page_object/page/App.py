from page_object.driver.AndroidClient import AndroidClient
from page_object.page.MainPage import MainPage


class App(object):
    @classmethod
    def main(cls):
        # 调用appium启动app
        AndroidClient.restart_app()
        return MainPage()

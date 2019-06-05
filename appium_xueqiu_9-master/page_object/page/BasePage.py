from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient

class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        # todo: 处理各类弹框
        return self.driver.find_element(*kv)


    def findByText(self,text)-> WebElement:
        return self.driver.find_element(By.XPATH, "//*[@text='"+ text +"']")

    def closeExistPopUp(self):
        _next_say = (By.XPATH, "//*[contains(@resource-id, 'md_buttonDefaultNegative')]")
        id = self.find(_next_say).get_attribute("text")
        flag = "下次再说" in id
        if flag==True:
            self.find(_next_say).click()


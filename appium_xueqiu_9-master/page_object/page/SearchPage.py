from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    def inputSearchBox(self, key):
        _search_box = (By.ID, "search_input_text")
        self.find(_search_box).send_keys(key)
        return self

    def add_a_stock(self,category):
        _add_attention = (By.XPATH,
                          "//*[contains(@resource-id,'stockCode') and contains(@text,'%s')]" %category +
                          "/../../..//*[contains(@resource-id,'add_attention')]")
        self.find(_add_attention).click()
        # self.closeExistPopUp()
        return self

    def isAdded(self,category):
        _followed_btn = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." %category +
                       "//*[contains(@resource-id, 'follow')]")

        id = self.find(_followed_btn).get_attribute("resourceId")
        print(id)
        return "followed" in id



    def gotoTable(self,key):
        _table = (By.XPATH, "//*[contains(@resource-id, 'ti_tab_indicator')]//*[@text='%s']" %key)
        self.find(_table).click()
        return self


    def addUser(self,key):
        _attent_user = (By.XPATH,"//*[contains(@resource-id,'user_name') and @text='%s']/../.." %key +
                                 "//*[contains(@resource-id,'add_attention')]")
        self.find(_attent_user).click()
        self.closeExistPopUp()
        return self


    def isAttented(self,key):
        _aleardy_attented = (By.XPATH, "//*[contains(@resource-id,'user_name') and @text='%s']/../.." %key+
                                       "//*[contains(@resource-id,'followed_btn')]")
        id = self.find(_aleardy_attented).get_attribute("resourceId")
        print(id)
        return "followed" in id






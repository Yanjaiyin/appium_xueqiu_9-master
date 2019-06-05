from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage
from page_object.page.SearchPage import SearchPage


class SelectPage(BasePage):
    _add_portfolio_stockBtn=(By.XPATH, "add_to_portfolio_stock")
    _create_cubeBtn=(By.ID, "action_create_cube")
    _search_input=(By.ID, "search_input_text")

    def addDefault(self):
        #todo: click "加入自选股"
        if self.find(SelectPage._add_portfolio_stockBtn):
            self.find(SelectPage._add_portfolio_stockBtn).click()
        return self

    def getPriceByName(self,name):
        #todo: get the price according the stock name
        priceCell = (MobileBy.XPATH,"//*[contains(@resource-id, 'stockName') and @text='%s']" %name +
                    "/../../..//*[contains(@resource-id, 'currentPrice')]")
        price = self.find(priceCell).text

        return float(price)

    def click_searchBtn(self,keys):
        self.find(SelectPage._create_cubeBtn).click()
        self.find(SelectPage._search_input)
        self.find(SelectPage._search_input).send_keys(keys)
        return SearchPage()






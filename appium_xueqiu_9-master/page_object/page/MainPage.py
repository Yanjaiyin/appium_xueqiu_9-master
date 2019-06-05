from selenium.webdriver.common.by import By

from page_object.page.SelectedPage import SelectPage
from page_object.page.BasePage import BasePage
from page_object.page.SearchPage import SearchPage

class MainPage(BasePage):
    _search_box=(By.ID, "home_search")

    def gotoSelect(self):
        #调用全局的driver对象使用webdriver api操纵app
        self.findByText("自选")
        self.findByText("自选").click()

        return SelectPage()


    def gotoSearch(self):
        self.find(self._search_box).click()
        return SearchPage()



import pytest

from page_object.page.App import App

class TestSelected(object):

    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()


    def test_price(self):
        assert self.mainPage.gotoSelect().getPriceByName("中国平安") == 77.18


    def test_add_stock(self):
        searchPage=self.mainPage.gotoSearch().inputSearchBox("alibaba")
        assert searchPage.isAdded("01688")==True
        # assert searchPage.isAdded("BABA")==False



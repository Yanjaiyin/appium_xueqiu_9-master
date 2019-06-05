import time

import pytest
from page_object.page.App import App



class TestSearch(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()


    def searchPage(self,key):
        return self.mainPage.gotoSearch().inputSearchBox(key)


    def test_add_stock(self):
        aliPage=self.searchPage("alibaba")
        time.sleep(3)
        if aliPage.isAdded("1688")==False:
            aliPage.add_a_stock("1688")
        assert aliPage.isAdded("1688")==True

        if aliPage.isAdded("BABA")==False:
            aliPage.add_a_stock("BABA")
        assert aliPage.isAdded("BABA")==True

    @pytest.mark.parametrize("key", ["alibaba"])
    def test_searchByUser(self,key):
        userPage=self.searchPage(key).gotoTable("用户")
        if userPage.isAttented(key)==False:
            userPage.addUser(key)
        assert userPage.isAttented(key)==True

    @pytest.mark.parametrize("key，code",
                             ["SH600036"
                              ""
                              ])
    def test_search_HS(self,key):
        zhaoshangPage = self.searchPage("zhaoshangyinhang")
        if zhaoshangPage.isAdded(key)==False:
            zhaoshangPage.add_a_stock(key)
        assert zhaoshangPage.isAdded(key)==True



    @classmethod
    def teardown_class(cls):
        print("test search page")


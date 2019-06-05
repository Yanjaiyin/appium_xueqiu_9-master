from telnetlib import EC

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

caps = {}

caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:7555"
caps["platformVersion"] = "6.0.1"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)

driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_icon' and @instance='6']").click()

driver.find_element_by_id("page_type_fund").click()
WebDriverWait(driver,30,1).until(expected_conditions.presence_of_all_elements_located(MobileBy.ACCESSIBILITY_ID,"已有蛋卷基金账户登录"))


driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()






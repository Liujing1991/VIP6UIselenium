from Common.BaseDriver import BaseDriver
from selenium.webdriver.common.by import By
from Common.Log import logger
from PO.BasePage import BasePage
from PO.LoginPage import LoginPage
from selenium.webdriver.support.ui import Select

import time

class CreateContribution(BasePage):
    _channel = (By.ID,'pChannelId')
    _change_channel = (By.XPATH,'//*[@id="pChannelId"]/option[9]')
    _create_menu = (By.XPATH,'/html/body/div[3]/div/div[1]/ul/li[2]/a/span[1]')
    _create_contribution = (By.XPATH,'/html/body/div[3]/div/div[1]/ul/li[2]/ul/li[1]/a')

    def __init__(self,driver):
        super().__init__(driver)
        logger.info('打开新建多媒体稿件页')

    def click_channel(self):
        self.by_find_element(*self._channel).click()

    def change_channel(self):
        cc = Select(self.driver.find_element_by_id("pChannelId"))
        cc.select_by_value(value='CHAL1494570464952106')

    def click_create_menu(self):
        self.by_find_element(*self._create_menu).click()

    def click_create_contribution(self):
        self.by_find_element(*self._create_contribution).click()

    def create_contribution(self):
        self.click_channel()
        self.change_channel()
        self.click_create_menu()
        self.click_create_contribution()

if __name__ == '__main__':
    driver = BaseDriver()
    driver.get('http://101.129.1.176/CMSMOBILE/cms/myConsole/myConsole.jsp')
    a = CreateContribution(driver)
    b = LoginPage(driver)
    time.sleep(6)
    b.login()
    a.create_contribution()
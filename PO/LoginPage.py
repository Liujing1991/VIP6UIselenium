'''
编写人：刘晶
编写日期：2020年11月26日
实现功能：登录页面对象类
    1.封装属性：登录页面的元素属性
    2.封装方法：
        2.1页面元素属性对应的操作方法
        2.2输入用户名
        2.3输入密码
        2.4点击登录
'''
import time
from selenium.webdriver.common.by import By
from PO.BasePage import BasePage
from common.BaseDriver import BaseDriver
from common.Log import logger

class LoginPage(BasePage):
    '''页面属性'''
    _username = (By.ID,'userName')
    _password = (By.ID,'password')
    _mobileSecurityCode = (By.ID,'mobileSecurityCode')
    _login_botton = (By.XPATH,'/html/body/div/div[2]/div[2]/div/form/button')

    def __init__(self,driver):
        super().__init__(driver)
        logger.info('进入登录页面')

    def input_username(self,username):
        '''元素操作方法'''
        self.by_find_element(*self._username).send_keys(username)

    def input_password(self,pwd):
        self.by_find_element(*self._password).send_keys(pwd)

    def input_mobileSecurityCode(self,mobileSecurityCode='1'):
        self.by_find_element(*self._mobileSecurityCode).send_keys(mobileSecurityCode)

    def click_login(self):
        self.by_find_element(*self._login_botton).click()

    def login(self,username='liujing',pwd='liujing123456',mobileSecurityCode='1'):
        self.input_password(username)
        self.input_password(pwd)
        self.input_mobileSecurityCode(mobileSecurityCode)
        self.click_login()

if __name__ == '__main__':
    driver = BaseDriver()
    driver.get('http://101.129.1.87/CMSMOBILE/')
    a = LoginPage(driver)
    time.sleep(10)
    a.login()

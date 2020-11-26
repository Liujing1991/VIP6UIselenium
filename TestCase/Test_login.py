'''

实现功能：登录界面的测试用例
'''
from common.BaseDriver import BaseDriver
import unittest,time
from PO.LoginPage import LoginPage
from common.Log import logger

class TestLogin(unittest.TestCase):

    def test_login_normal(self):
        self.driver = BaseDriver()
        self.url = 'http://101.129.1.87/CMSMOBILE/'
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.login()
        time.sleep(10)
        logger.info('登录测试完毕')

if __name__ == '__main__':
    unittest.main()

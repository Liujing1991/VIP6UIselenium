'''

实现功能：登录界面的测试用例
'''
from Common.BaseDriver import BaseDriver
import unittest
from PO.LoginPage import LoginPage
from Common.Log import logger
import os
from Common.Public import Public

class TestLogin(unittest.TestCase):

    def test_login_normal(self):
        self.driver = BaseDriver()
        self.url = 'http://101.129.1.87/CMSMOBILE/'
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.login()
        assert '菜单管理页' == self.driver.title
        logger.info('登录测试完毕')
        # self.driver.quit()


if __name__ == '__main__':
    #每个报告在此生成
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)
    file = os.path.abspath(__file__)
    Public().gen_unittest_report(suite, file)

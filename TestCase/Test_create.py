
from Common.BaseDriver import BaseDriver
import unittest
from PO.LoginPage import LoginPage
from PO.CreateContribution import CreateContribution
from Common.Log import logger
from PO.BasePage import BasePage
import os
from Common.Public import Public

class TestCreate(unittest.TestCase):

    def test_create(self):
        self.driver = BaseDriver()
        url = 'http://101.129.1.87/CMSMOBILE'
        self.driver.get(url)
        login = LoginPage(self.driver)
        login.login()
        create = CreateContribution(self.driver)
        create.create_contribution()
        print(self.driver.title)

        logger.info('已进入新建多媒体')
        handle1 = self.driver.current_window_handle
        print('第一个窗口的ID：',handle1)
        handle2 = self.driver.window_handles[1]
        self.driver.switch_to.window(handle2)
        print(self.driver.title)
        assert '新建多媒体' == self.driver.title

        b = BasePage(self.driver)
        b.scrollmid1()


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCreate)
    file = os.path.abspath(__file__)
    Public().gen_unittest_report(suite, file)

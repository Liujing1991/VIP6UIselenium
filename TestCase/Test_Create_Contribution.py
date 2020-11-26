
import unittest
from common.BaseDriver import BaseDriver
from PO.CreateContribution import CreateContribution
from common.Log import logger
from PO.LoginPage import LoginPage
class TestCreateContribution(unittest.TestCase):
    def test_create_contribution(self):
        self.driver = BaseDriver()
        self.url = 'http://101.129.1.87/CMSMOBILE/cms/myConsole/myConsole.jsp'
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.login()
        create_contri_page = CreateContribution(self.driver)
        create_contri_page.create_contribution()
        logger.info('点击新建多媒体稿件')

if __name__ == '__main__':
    unittest.main()
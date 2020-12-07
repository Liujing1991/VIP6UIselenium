

from PO.CreateArtPage import CreateArtPage
from PO.CreateContribution import CreateContribution
from PO.LoginPage import LoginPage
from Common.BaseDriver import BaseDriver
import unittest
import os
from Common.Public import Public

class TestCreateArt(unittest.TestCase):

    def test_create_art(self):
        self.driver = BaseDriver()
        url = 'http://101.129.1.87/CMSMOBILE'
        self.driver.get(url)
        a = LoginPage(self.driver)
        b = CreateContribution(self.driver)
        c = CreateArtPage(self.driver)
        a.login()
        b.create_contribution()
        c.switch_window()
        c.create_art()

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateArt)
    file = os.path.abspath(__file__)
    Public().gen_unittest_report(suite, file)
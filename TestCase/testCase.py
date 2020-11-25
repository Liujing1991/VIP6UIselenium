import unittest,time

from selenium.webdriver.common.by import By

from common.BaseDriver import BaseDriver

class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('执行setUpClass方法')
        cls.driver = BaseDriver()

    def setUP(self) -> None:
        print('执行setUp方法')

    def test_login(self):
        print('准备登录')
        #隐式等待5秒，5秒内渲染出来不再等待
        self.driver.implicitly_wait(5)
        #最大化窗口
        self.driver.maximize_window()
        #打开玩安卓网页
        self.driver.get('https://www.wanandroid.com')
        #点击登录按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/ul[1]/li[1]/a').click()
        #xpath定位用户名输入框并输入用户名
        self.driver.find_element_by_xpath('//*[@id="loginDialog"]/div/input[1]').send_keys('liujingjing')
        #xpath定位密码输入框并输入密码
        self.driver.find_element_by_xpath('//*[@id="loginDialog"]/div/input[2]').send_keys('123456')
        #xpath定位登录按钮并点击
        self.driver.find_element_by_xpath('//*[@id="loginDialog"]/div/p[3]/span').click()
        #css定位广场并点击
        # self.driver.find_element_by_css_selector('body > div.e > div.e_container.mt30 > div.main_content_l > div:nth-child(3) > h2 > a:nth-child(3)').click()

        # self.driver.get('https://www.wanandroid.com/navi')
        # self.driver.find_element_by_xpath('//a[@href="/navi"]').click()
        # content = self.driver.find_element_by_xpath('/html/body/div[1]/div[8]/div/div[2]/div[2]/div[2]').get_attribute('textContent')
        # print('获取到的元素：', content)
        time.sleep(5)

    def tearDown(self) -> None:
        print('执行tearDown方法')

    @classmethod
    def tearDownClass(cls) -> None:
        print('执行tearDown方法')
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

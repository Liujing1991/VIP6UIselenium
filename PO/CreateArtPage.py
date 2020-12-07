import time
from selenium.webdriver.common.by import By
from Common.Log import logger
from PO.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from Common.BaseDriver import BaseDriver
from PO.LoginPage import LoginPage
from PO.CreateContribution import CreateContribution

class CreateArtPage(BasePage):

    _articleTitle = (By.ID,'articleTitle')
    _tag = (By.ID,'TagX1483686773330104')
    _iframe = (By.ID,'ueditor_1')
    _editor = (By.XPATH, '/ html / body')
    _image = (By.XPATH,'//*[@id="basicContent"]/div/div[1]/div[3]/div[2]/form/div/div[1]/div[1]/div/div')
    _local_up= (By.ID,'imgFileOne')
    _image_path = 'C:\\Users\\LiYs\\Pictures\\123.jpg'
    _apply = (By.XPATH,'//*[@id="batchUpload"]/div/a[1]')
    _preview = (By.ID,'preview')
    _fabuBtn = (By.ID,'fabuBtn')
    _progressList = (By.ID,'progressList')
    _progressID = 'Apve1579060169560186'
    _launchSure = (By.ID,'launchSure')
    _sure = (By.XPATH,'/html/body/div[7]/div[2]/a[1]')

    def __init__(self,driver):
        super().__init__(driver)
        logger.info('进入新建多媒体页')

    def input_title(self,title):
        self.by_find_element(*self._articleTitle).send_keys(title)

    def tag_click(self):
        self.by_find_element(*self._tag).click()

    def input_art(self,art):
        iframe = self.by_find_element(*self._iframe)
        self.driver.switch_to.frame(iframe)
        self.by_find_element(*self._editor).send_keys(art)
        self.driver.switch_to.default_content()

    def up_image(self,path):
        self.by_find_element(*self._image).click()
        time.sleep(3)
        self.by_find_element(*self._local_up).send_keys(path)
        self.by_find_element(*self._apply).click()

    def preview(self):
        self.by_find_element(*self._preview).click()

    def fabu(self):
        self.by_find_element(*self._fabuBtn).click()

    def progress(self):
        st = Select(self.by_find_element(*self._progressList))
        st.select_by_value(self._progressID)

    def launchSure(self):
        self.by_find_element(*self._launchSure).click()

    def sure_close(self):
        self.by_find_element(*self._sure).click()

    def switch_window(self):
        handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(handle)

    def create_art(self,title = 'LJtest',art = 'test123',path =_image_path):
        self.input_title(title)
        self.scrollmid1()
        self.tag_click()
        self.input_art(art)
        self.scrollmid2()
        # self.up_image(path)
        self.preview()
        self.fabu()
        self.progress()
        self.launchSure()
        self.sure_close()

if __name__ == '__main__':
    driver = BaseDriver()
    driver.get('http://101.129.1.87/CMSMOBILE')
    a = LoginPage(driver)
    b = CreateContribution(driver)
    c = CreateArtPage(driver)
    a.login()
    b.create_contribution()
    c.switch_window()
    c.create_art()





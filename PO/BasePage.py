'''
编写人：刘晶
编写日期：2020年11月26日
实现功能：所有page页面的基类；提供统一的方法
    1.构造方法：init
        1.1接收test用例传入的driver
    2.定位方法：find_element
        2.1二次封装find_element方法，加入超时判断
    3.打开方法：get
        3.1二次封装get方法，一次性判断，进入的页面是否成功
'''
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.Log import logger


class BasePage(object):

    def __init__(self, driver):
        # 接收test传入的driver对象
        self.driver = driver

    def by_find_element(self, *item):
        try:
            logger.info('定位的目标元素：%s' % str(item))
            # 确保元素是可见的
            # 注意：以下入参为元组的元素，需要加*，Python存在这种特性，就是将入参放在元组里

            element = WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_element_located(item))
            return element

        except Exception as msg:
            logger.info('系统提示异常：%s' % msg)
            logger.info(u'页面中未找到%s元素' % str(item))

    '''当页面上的元素超过一屏后，想操作屏幕下方的元素，是不能直接定位到，会报元素不可见；
    可以先让页面直接跳到元素出现的位置，然后就可以操作了。需要借助JS去实现'''
    def focus(self,*item):
        try:
            logger.info('聚焦元素')
            target = self.driver.by_find_element(*item)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
        except Exception as msg:
            logger.info('聚焦元素失败，提示%s' % msg)

    def get(self,url):
        try:
            self.driver.get(url)
            self.driver.maximized_window()

        except Exception as msg:
            print(u'%s 页面打开失败' % url)
            logger.info('异常显示：%s' % msg)


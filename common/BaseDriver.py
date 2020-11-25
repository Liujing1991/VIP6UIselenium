'''
编写人：刘晶
编写日期：2020年11月25日
实现功能：封装用例依赖的driver
    1.方法：BaseDriver
        1.1准备浏览器，设置driver的参数（有无界面/取消自动化提示）
        1.2根据config.ini配置文件读取driver配置是否需要有界面运行
        1.3返回driver对象，提供给测试用例调用


'''
import time
from selenium import webdriver
from common.ReadConfig import ReadConfig

def BaseDriver():
    #1-实例化ChromeOption对象
    chrome_option = webdriver.ChromeOptions()
    #实例化ReadConfig()，读取ini文件中的配置
    rc = ReadConfig()
    gui = rc.get_driver('gui')
    # 判断config配置是否需要有界面运行
    if gui.lower()=='yes':
        # logger.info('chrome 有界面运行')
        # 消除自动化控制提示
        chrome_option.add_experimental_option('useAutomationExtension',False)
        chrome_option.add_experimental_option("excludeSwitches",['enable-automation'])
        # 最大化窗口参数
        chrome_option.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_option)

    else:
        # 无界面参数--headless
        chrome_option.add_argument('--headless')
        # logger.info('chrome 有界面运行')
        # 消除自动化控制提示
        chrome_option.add_experimental_option('useAutomationExtension', False)
        chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 最大化窗口参数
        chrome_option.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_option)

    return driver

if __name__ == '__main__':
    driver = BaseDriver()
    url = ReadConfig().get_driver('url1')
    print(url)
    driver.get('http://101.129.1.176/CMSMOBILE/')
    # driver.get(url)

# def BaseDriver():
#     #1-实例化ChromeOption对象
#     chrome_option = webdriver.ChromeOptions()
#     #2-通过该对象添加参数
#     #2.1-隐身模式（无痕模式）参数
#     chrome_option.add_argument('--incognito')
#     #2.2-最大化窗口参数
#     chrome_option.add_argument('--start-maximized')
#
#     #3-以下两个事消除“自动化控制提示”的参数
#     chrome_option.add_experimental_option('useAutomationExtension',False)
#     chrome_option.add_experimental_option("excludeSwitches",['enable-automation'])
#
#     #4-最后Chrome里面需要传递该对象信息
#     driver = webdriver.Chrome(options=chrome_option)
#     return driver
#
# if __name__ == '__main__':
#     driver =BaseDriver()
#     # content = driver.find_element_by_xpath('//*[@id="272"]').get_attribute('innerHTML')
#     # print('获取到的元素：',content)
#     driver.implicitly_wait(5)
#     # 最大化窗口
#     driver.maximize_window()
#     # 打开玩安卓网页
#     driver.get('http://126.com/')
#     #跳入框架
#     xp = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
#     driver.switch_to.frame(xp)
#     #输入邮箱账号
#     driver.find_element_by_name('email').send_keys('liujing')
#     time.sleep(2)
#     #跳出框架
#     driver.switch_to.default_content()

# driver = webdriver.Chrome()
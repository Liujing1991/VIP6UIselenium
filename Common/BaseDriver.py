'''
编写人：
    刘晶
编写日期：
    2020年11月19日
实现功能：封装用例依赖的driver
    1.方法：BaseDriver
        1.1 准备浏览器，设置driver的参数（无界面/取消自动化提示）
        1.2 根据config.ini配置文件读取driver配置是否需要有界面运行
        1.3 返回diver对象，提供给测试用例调用
'''
from selenium import webdriver
from Common.Log import logger
import time
from Common.ReadConfig import ReadConfig



def BaseDriver():
    """准备对外依赖的driver"""
    opt = webdriver.ChromeOptions()
    rc = ReadConfig()
    gui = rc.get_driver('gui')
    if gui.lower() == 'yes':
        logger.info('chrome 有界面运行')
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        opt.add_experimental_option("prefs", prefs)  ##关掉密码弹
        opt.add_experimental_option('useAutomationExtension',False)
        opt.add_experimental_option('excludeSwitches',['enable-automation'])
        opt.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=opt)
    else:
        logger.info('chrome 无界面运行')
        opt.add_argument('--headless')
        opt.add_experimental_option('useAutomationExtension', False)
        opt.add_experimental_option('excludeSwitches', ['enable-automation'])
        opt.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=opt)
    return driver

if __name__ == '__main__':
    url = ReadConfig().get_driver('url')
    driver = BaseDriver()
    driver.get(url)
    # driver.get('http://101.129.1.87/CMSMOBILE')
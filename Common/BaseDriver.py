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
    #实例化启动浏览器参数
    opt = webdriver.ChromeOptions()
    #读取ini文件中gui的值（是否有界面运行）
    rc = ReadConfig()
    gui = rc.get_driver('gui')
    if gui.lower() == 'yes':
        logger.info('chrome 有界面运行')

        # 关掉密码弹窗
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        opt.add_experimental_option("prefs", prefs)

        # 关掉自动化控制提示
        opt.add_experimental_option('useAutomationExtension',False)
        opt.add_experimental_option('excludeSwitches',['enable-automation'])

        #隐身（无痕）模式
        opt.add_argument('--incognito')

        # 最大化运行（全屏窗口）
        opt.add_argument('--start-maximized')

        #启动浏览器
        driver = webdriver.Chrome(options=opt)
    else:
        logger.info('chrome 无界面运行')
        opt.add_argument('--headless')
        opt.add_experimental_option('useAutomationExtension', False)
        opt.add_experimental_option('excludeSwitches', ['enable-automation'])
        opt.add_argument('--start-maximized')   #最大化运行（全屏窗口）
        driver = webdriver.Chrome(options=opt)
    return driver

if __name__ == '__main__':
    url = ReadConfig().get_driver('url')
    driver = BaseDriver()
    driver.get(url)
    # driver.get('http://101.129.1.87/CMSMOBILE')
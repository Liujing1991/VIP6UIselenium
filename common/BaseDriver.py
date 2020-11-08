'''
basedriver练习启动参数
'''

from selenium import webdriver

#1-实例化ChromeOption对象
chrome_option = webdriver.ChromeOptions()
#2-通过该对象添加参数
#2.1-隐身模式（无痕模式）参数
chrome_option.add_argument('--incognito')
#2.2-最大化窗口参数
chrome_option.add_argument('--start-maximized')

#3-以下两个事消除“自动化控制提示”的参数
chrome_option.add_experimental_option('useAutomationExtension',False)
chrome_option.add_experimental_option("excludeSwitches",['enable-automation'])

#4-最后Chrome里面需要传递该对象信息
driver = webdriver.Chrome(options=chrome_option)

# driver = webdriver.Chrome()
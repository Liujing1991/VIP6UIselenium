'''
读取框架的配置
'''

import configparser
import os

pro_dir = os.path.dirname(os.path.dirname(__file__))
class ReadConfig(object):
    def __init__(self):
        # 属性（读取文件参数）
        self.conf = configparser.ConfigParser()
        #获取配置文件的路径
        self.file_path = pro_dir + "\\" + 'config.ini'
        print(self.file_path)
        self.data = self.conf.read(self.file_path,encoding='utf-8-sig')
        print(self.data,'------------')

    def get_driver(self,option='all'):
        """获取DRIVER下的全部或某一个option
        不传参就是默认参数option='all'：
        传参如‘url’:
        """
        if option =='all':
            return self.conf.items('DRIVER')
        else:
            return self.conf.get('DRIVER',option)

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_driver('url'))
    print(type(rc.get_driver('url')))
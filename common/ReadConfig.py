'''

编写人：刘晶
编写日期：2020年7月17日
实现功能：
    读取框架的配置
'''

import configparser,os

class ReadConfig(object):
    def __init__(self):
        # 实例化导入包的类
        self.conf = configparser.ConfigParser()
        # 定位目标文件
        file = os.path.dirname(os.path.dirname(__file__)) + "/config.ini"
        print('-----------',file)
        self.conf.read(file,encoding='utf-8-sig')

    def get_driver(self,option='all'):
        """
        获取DRIVER中的全部或某个option
        option='all' 是默认参数，调用时不传参就默认是option='all'
        如果传参就默认获取某一个option
        :param option: 'url'或者不传参
        :return: all：[('browser', 'chrome'), ('gui', 'yes'), ('url', "'http://101.129.1.176/CMSMOBILE/'")]
                单个：'http://101.129.1.176/CMSMOBILE/'
        """
        if option == 'all':
            return self.conf.items('DRIVER')
        else:
            return self.conf.get('DRIVER',option)


if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_driver())
    print(rc.get_driver('url'))

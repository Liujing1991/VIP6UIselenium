'''
编写人：刘晶
编写日期：2020年11月25日
实现功能：封装日志模块
    日志级别：
            CRITICAL
            ERROR
            WARNING
            INFO
            DEBUG
    1.构造方法：__init__
        1.1设置日志级别
        1.2创建logger
        1.3判断logger是否已经添加句柄，避免重复打印问题
        1.4添加控制台日志句柄和文件日志句柄

    2.私有方法：_get_console_handler
        2.1创建控制台日志句柄
    3.私有方法：_get_file_handler
        3.1创建文件日志句柄
    4.实例方法：get_logger
        4.1返回logger公外部使用
    5.预设实例对象，使用时直接导入，作为单例使用，方便其他模块直接打印日志
'''

import logging,os,time

pro_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Logger(object):
    def __init__(self):
        # 定义logger的基本设置
        # 指定日志输出格式,formatter ：格式器的意思
        self._formatter = logging.Formatter('%(asctime)s-'
                                  '%(levelname)s-'
                                  '%(filename)s-'
                                  '%(threadName)s-'
                                  '[line:%(lineno)d]-'
                                  '%(name)s-'
                                  '日志信息：%(message)s')
        #指定日志输出目录
        self._log_dir = pro_dir + "\\" + "Logs"

        #创建日志实例，日志名称用来唯一确定一个日志对象
        self._logger = logging.getLogger('test111_log')
        self._logger.setLevel(logging.INFO)
        #判断是否已经有实例对象，如果没有的话再添加句柄，防止日志重复打印
        if not self._logger.handlers:
            #添加日志句柄
            self._logger.addHandler(self._get_console_handler())
            self._logger.addHandler(self._get_file_handler())

    def _get_console_handler(self):
        #设置控制台输出句柄
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self._formatter)
        return ch
    def _get_file_handler(self):
        #设置文件输出句柄
        timestr = time.strftime('%Y-%m-%d')
        file = self._log_dir + "\\" + "LJ_test_" + timestr + "_log.txt"
        #输出到file
        fh = logging.FileHandler(file,mode='a',encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
        fh.setLevel(logging.INFO)
        fh.setFormatter(self._formatter)
        return fh

    def get_logger(self):
        # 对外提供logger实例
        return self._logger

#预设实例，作为单例，给外部使用
logger = Logger().get_logger()

if __name__ == '__main__':
    logger.info('111111111111111')
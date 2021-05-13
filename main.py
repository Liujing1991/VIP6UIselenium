


# import unittest,os,HTMLTestRunner,time
#
# def creat_suite():
#
#     # 获取testcase所在目录
#     startDir = os.path.dirname(__file__) + "/TestCase"
#     # discover自动查找路径下的test开头的py文件
#     suite = unittest.defaultTestLoader.discover(start_dir=startDir,pattern='Test*.py')
#
#     #时间戳
#     timestr = time.localtime(time.time())
#     times = time.strftime('%Y-%m-%d-%H-%M',timestr)
#     # 生成的报告路径和名称
#     filename = os.path.dirname(__file__) + "/TestReport/" + times + "report.html"
#
#     # fp = open(filename,'wb')
#     # runner = HTMLTestRunner.HTMLTestReportCN(stream=fp,title='接口测试报告',description='复习生成html测试报告')
#     # runner.run(suite)
#     # fp.close()
#
#     # 使用with open不需要再关闭文件
#     with open(filename,'wb') as file:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='测试报告',description='简介')
#         runner.run(suite)
#
# if __name__ == '__main__':
#     # # 每次运行前删除report目录下的所有报告
#     # # 找到报告所在目录
#     # path = os.path.dirname(os.path.dirname(__file__)) + "/report/"
#     # # 获取目录下的所有文件和目录，生成列表
#     # listdir = os.listdir(path)
#     # # 遍历列表
#     # for f in listdir:
#     #     #先将遍历到的文件和父目录拼接一下，防止有斜杠错误
#     #     file_path = os.path.join(path,f)
#     #     # 判断，如果是个文件，就删除
#     #     if os.path.isfile(file_path):
#     #         os.remove(file_path)
#     #执行creat_suite方法，会将testcase生成套件并执行用例，并生成HTML报告到report目录下
#     creat_suite()













import threading
import time

from Common.Public import Public
from Common.Log import logger
import os,subprocess
from Common.MergeReport import MergeReport



cur_dir = Public().get_basedir()
case_dir = cur_dir + "\\" + 'TestCase\\'


def get_test_list():
    """
    获取框架内要运行的所有用例文件名称
    :return: 返回用例组成的列表
    """
    t_list = os.listdir(case_dir)
    return t_list


def run_test(name):
    """
    多线程调用的目标函数
    :param name:
    :return:
    """
    #通过控制信号量，来控制同时启动的线程最大数量
    with pool_sema:
        print('run py start')
        logger.info("python %s%s " % (case_dir,name))
        subprocess.run("python %s%s " % (case_dir,name))
        print('run py end')


if __name__ == '__main__':
    start_time = time.time()
    tlist = []
    test_list = get_test_list()
    # 设置启动线程的最大数量
    maxconnections = 4
    pool_sema = threading.BoundedSemaphore(value=maxconnections)

    logger.info('运行的测试列表：%s' % str(tlist))
    for i in test_list:
        # 创建线程
        # target用来调用线程函数run_test；args读取到每一个测试用例作为参数传给run_test；name是给线程命名
        t = threading.Thread(target=run_test, args=(i,), name='Thread' + str(test_list.index(i)))
        #守护线程
        t.setDaemon(True)
        tlist.append(t)

    # 启动线程
    for i in tlist:
        i.start()

    #主线程等待子线程
    for i in tlist:
        i.join()
    time.sleep(5)

    end_time = time.time()
    elpase_time = end_time - start_time
    logger.info(int(elpase_time))

    d, h, m, s = Public().time_format(int(elpase_time))
    mr = MergeReport()
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    elpase = ' %s 时 %s 分 %s 秒' % (h, m, s)
    mr.merge(start, elpase)
    logger.info('开始和持续时间：%s%s' % (start, elpase))
    print('主线程结束，程序运行时长 %s天 %s小时 %s分钟 %s秒' % (d, h, m, s))
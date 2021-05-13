"""
1--导入包
2--定义多线程执行的函数
3--创建多线程
4--启动多线程
"""


import threading
from threading import Thread
import time

#第一步，封装一个函数，多线程启动的就是这个函数
def run():
    #获取当前线程的名称，创建线程的时候，实例化传参传name=xxx，当前方法就可以接收到
    threadName = threading.current_thread().getName()
    print('线程名字是：',threadName)

    time.sleep(1)
    print('执行函数的第一步')

    time.sleep(1)
    print('执行函数的第二步')

if __name__ == '__main__':
    # target用来传递调用的函数名；name参数用来指定线程名，如果不传，默认显示Thread-n
    t1 = threading.Thread(target=run,name='线程一')
    t2 = threading.Thread(target=run,name='线程二')

    #启动线程
    t1.start()
    t2.start()
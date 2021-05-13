"""
多线程之间，，共享全局变量，在线程1执行的时候，线程2也在执行，2个线程共同使全局变量发生变化
请参考互斥锁，可解决此问题
"""

import threading,time

num = 1000000

def fun1():
    # 函数内使全局变量发生变化前，先声明是全局变量
    global num
    for i in range(500000):
         num -= 1
    print('in fun1 num is : %d' % num)

def fun2():
    # 函数内使全局变量发生变化前，先声明是全局变量
    global num
    for i in range(500000):
         num -= 1
    print('in fun2 num is : %d' % num)

if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()


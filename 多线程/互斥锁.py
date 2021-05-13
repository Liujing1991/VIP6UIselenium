"""
解决共享全局变量问题，在线程1执行时，将全局变量锁起来，线程1执行完再释放
"""
from threading import Thread,Lock

num = 1000000

def fun1():
    # 函数内使全局变量发生变化前，先声明是全局变量
    global num
    # 将全局变量上锁
    lock.acquire()
    for i in range(500000):
         num -= 1
    print('in fun1 num is : %d' % num)
    lock.release()

def fun2():
    # 函数内使全局变量发生变化前，先声明是全局变量
    global num
    lock.acquire()
    for i in range(500000):
         num -= 1
    print('in fun2 num is : %d' % num)
    lock.release()

if __name__ == '__main__':
    # 实例化Lock类
    lock = Lock()
    #创建线程
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    #启动线程
    t1.start()
    t2.start()

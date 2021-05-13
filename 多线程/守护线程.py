import threading,time

#多线程启动的就是这个函数，参数接收的是创建线程时args参数
def run(n):
    #获取当前线程的名称，创建线程的时候，实例化传参传name=xxx，当前方法就可以接收到
    threadName = threading.current_thread().getName()
    print('线程名字是：',threadName)

    time.sleep(1)
    print('执行函数的第1步',n)

    time.sleep(1)
    print('执行函数的第2步',n)

if __name__ == '__main__':
    # t = threading.Thread(target=run,args=('参数1',))
    # t.setDaemon()  #守护线程
    # t.start()  #启动线程
    # t.join()  #等待线程

    # ------------- 用循环的方式启动多个线程----------

    tlist = []
    # 把子线程设置为守护线程，必须在启动线程start()之前设置
    for i in range(1,3):
        t = threading.Thread(target=run,name="线程"+str(i),args=("参数"+str(i),))
        t.setDaemon(True)
        tlist.append(t)

    for t in tlist:
        # 启动线程
        t.start()
    for t in tlist:
        # 设置主线程等待子线程，不然主线程跑完了，子线程还没跑完，报告生成不完整
        t.join()
    print('end')
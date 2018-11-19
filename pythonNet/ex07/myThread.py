from threading import Thread
from time import ctime,sleep

class MyThread(Thread):
    '''这是自定义线程类'''
    def __init__(self, target, args=(), kwargs={}, name='Thread-1'):
        super().__init__()
        self.fun = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    def run(self):
        self.fun(*self.args,**self.kwargs)





# 测试函数 函数形式不定       
# 形参可以为任意多个, 名称随意

def pllayer(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song , ctime()))
        sleep(sec)


t = MyThread(target=pllayer,args=(3,),kwargs={'song':'年少有为'},name='Tedu')
t.start()
t.join()
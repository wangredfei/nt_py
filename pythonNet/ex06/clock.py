from multiprocessing import Process
from time import sleep,ctime

class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载父类init

    def time1(self):
        print('开始倒计时')
        for i in range(self.value):
            sleep(1)
            print(ctime())

    def time2(self):
        print("倒计时结束")
    # 重写run()方法
    def run(self):
        self.time1()
        self.time2()

# 创建进程对象
p = ClockProcess(5)
p.start()
p.join()
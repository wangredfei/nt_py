import multiprocessing as mp
from time import sleep,ctime

def fun():
    print("执行子进程")
    sleep(2)
    print("子进程执行完毕")

# 创建进程对象
p = mp.Process(target = fun)

# 启动进程
p.start()

for i in range(3):
    sleep(1)
    print(ctime())

# 回收进程
p.join()
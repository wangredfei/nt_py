from multiprocessing import Process,Pipe
import os,time 

# fd1,fd2 = Pipe()
fd1,fd2 = Pipe(False)


def fun(name):
    time.sleep(3)
    fd1.send("hello"+name)


jobs = []
for i in ['an','kong','zhang','chen']:
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(4):
    # 从管道读取内容
    data = fd2.recv()
    print(data)

for i in jobs:
    i.join()


'''
# 两个子进程
from multiprocessing import Process,Pipe
import os,time 

fd1,fd2 = Pipe()

def fun(name):
    time.sleep(3)
    fd1.send("hello"+name)

def fun2():
    data = fd2.recv()
    print(data)

p = Process(target=fun, args=('hahahaha',))
pp = Process(target=fun2)

p.start()
pp.start()

p.join()
pp.join()
'''
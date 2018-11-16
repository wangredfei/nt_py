from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = Process(target=tm, name="ANAN")


p.daemon = True # 使子进程随主进程结束

p.start()
print("name: ",p.name)
print("pid:",p.pid)
print("alive:",p.is_alive())

# p.join()
import threading
from time import sleep
import os
 
a = 1
# 线程函数
def music():
    global a
    print(a)
    a = 1000
    for i in range(3):
        sleep(2)
        print("沙漠骆驼",os.getpid())

# 创建线程对象
t = threading.Thread(target=music)
t.start()
for i in range(3):
    sleep(3)
    print("aaa",os.getpid())
print(a)
t.join()
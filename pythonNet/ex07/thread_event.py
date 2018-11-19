from threading import Thread, Event
from time import sleep

s = None # 作为通信变量
e = Event()

def bar():
    print("Bar bbbb")
    global s
    s = '啊啊啊啊啊'
    e.set()

b = Thread(target=bar)
b.start()
print("suo对口令,就是自己人")
e.wait()
if s == "啊啊啊啊啊":
    print("yes")
else :
    print("kill")
b.join()
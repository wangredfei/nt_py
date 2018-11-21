import gevent
from time import sleep

def foo(a,b):
    print("Running in foo ",a,b)
    gevent.sleep(2)
    print("foo end")
def fff():
    print("Running in fff ")
    gevent.sleep(3)
    print("fff end")
f = gevent.spawn(foo,1,2)
ff = gevent.spawn(fff)
# for i in range(10):
#     sleep(2)
#     print("======")
gevent.joinall([f,ff])
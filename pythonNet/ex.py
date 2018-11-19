# import socket

# sockfd = socket.socket(
#     socket.AF_INET,
#     socket.SOCK_STREAM,
#     proto=0
# )

# # 绑定服务器
# sockfd.bind(("0.0.0.0",9999))

# while 1: 
#     sockfd.listen(2)
#     print("wait to connect....")
#     connfd, addr = sockfd.accept()
#     data = connfd.recv(1024)
#     print(data)
#     if data == b"q":
#         break
#     n = connfd.send("nihao".encode())
#     print("zijieshu = ", n)

# connfd.close()
# sockfd.close()

# from socket import *
# sockfd = socket()
# sockfd.bind(("0.0.0.0",3544))
# f = open("bbb.html","rb")

# sockfd.listen(5)
# print("wait....")
# while 1:
#     connfd, addr = sockfd.accept()
#     a = connfd.recv(4098)
#     data = f.read()
#     connfd.send(data)
# connfd.close()
# f.close()
# sockfd.close()
# l = [[1,2],[3,4],[5,6]]
# print([z for y in l for z in y])

# from socket import *
# sockfd = socket(AF_INET,SOCK_DGRAM)
# sockfd.bind(('0.0.0.0',8080))
'''
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


# ISO 网络通信标准化流程 : 
# 七层模型 
# 应用层 : 提供用户服务,具体功能由程序实现
# 表示层 : 数据的压缩优化和加密 
# 会话层 : 建立应用链接,选择合适的传输方式
# 传输层 : 提供传输服务,流量控制 
# 网络层 : 路由选择,网络互联
# 链路层 : 进行数据交换,控制具体的消息收发,链路链接
# 物理层 : 提供物理硬件传输, 网卡, 接口设置,传输介质


'''
# TCP套接字服务端

from socket import *
s = socket(family=AF_INET,type=SOCK_STREAM,proto=0)
s.bind(('0.0.0.0',8388))
s.listen(5)
while 1:
    try:
    c, addr = s.accept()
    except KeyboardInterrupt:
        break
    while True:
        print("wait....")
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        n = c.send("Recive: ".encode())
        print(n)
c.close()
s.close()
'''

# # UDP 服务端 
# from socket import *

# sockfd = socket(AF_INET,SOCK_DGRAM)
# sockfd.bind(('0.0.0.0',9999))

# while 1:
#     # 注意收发参数
#     data, addr = sockfd.recvfrom(1024)
#     if not data:
#         break
#     print(data.decode())
#     sockfd.sendto("你好".encode(),addr)

# sockfd.close()
# --------------------------------------
'''
from socket import * 
import time 

# 创建UDP套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
# 设置可以广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
# 地址
dest = ('192.168.43.255',8888)

while 1:
    time.sleep(2)
    sockfd.sendto("你好".encode(),dest)
sockfd.close()
'''
# ---------------------------------
'''
from socket import * 
s = socket()
s.bind(('0.0.0.0',8818))
s.listen(4)
# s.setblocking(False)
s.settimeout(5)
while True: 
    c, addr = s.accept()
    data = c.recv(1024)
    print(data.decode())
    c.send("recive".encode())
c.close()
s.close()
'''
# # ---------------------------------
# # IO 多路服用select
# from socket import * 
# from select import select

# # 创建套接字
# s = socket()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
# s.bind(('0.0.0.0',8888))
# s.listen(5)

# # 创建监听列表
# rlist=[s]
# wlist=[]
# xlist=[]


# while True:
#     # 设置监听
#     rl,wl,xl = select(rlist, wlist, xlist)

#     for r in rl:
#         # 判断是否是等于s
#         if r == s:
#             c, addr = r.accept()
#             rlist.append(c)
#         else:
#             data = r.recv(1024)
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#                 continue
#             print("收到:",data.decode())

#             wlist.append(r)
#     for w in wl:
#         w.send(b'OK')
#         wlist.remove(w)
#     for x in xl:
#         pass

from multiprocessing import Process,Value
import time
import random 

# 创建共享内存
money = Value('i',5000)

def boy():
    for i in range(30):
        time.sleep(0.05)
        # 操作共享内存
        money.value += random.randint(1,1599) 
def gril():
    for i in range(30):
        time.sleep(0.05)
        money.value -= random.randint(50,1000)

p = Process(target=boy)
pp = Process(target=gril)
p.start()
pp.start()
p.join()
pp.join()
print(money.value)
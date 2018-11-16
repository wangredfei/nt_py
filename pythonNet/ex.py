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
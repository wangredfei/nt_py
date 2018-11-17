'''
TCP套接字服务端

from socket import *

s = socket(
    family=AF_INET,
    type=SOCK_STREAM,
    proto=0
)

s.connect(('127.0.0.1',8388))

while True:
    try:
        data = input(">>>")
    except KeyboardInterrupt:
        break
    if not data:
        break
    s.send(data.encode())
    data = s.recv(1024)
    print(data.decode())
s.close()
'''

# # UDPclient
# from socket import *
# import sys

# sockfd = socket(AF_INET,SOCK_DGRAM)
# print(sys.argv)
# HOST = sys.argv[1]
# PORT = sys.argv[2]
# ADDR = (str(HOST),int(PORT))

# while 1 : 
#     data = input(">>>")
#     if not data:
#         break
#     sockfd.sendto(data.encode(),ADDR)
#     data, addr = sockfd.recvfrom(1024)
#     print(data.decode())
# sockfd.close()
# -----------------------------------------
'''
from socket import * 
s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('0.0.0.0',8888))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("msg:",msg.decode())
    except KeyboardInterrupt:
        break

d.close()
'''


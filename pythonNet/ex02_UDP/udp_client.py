import sys
from socket import *


print(sys.argv)
HOST , PORT = sys.argv[1],int(sys.argv[2])
ADDR = (HOST,PORT)

# 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)


# 收发消息
while True: 
    data = input("Msg:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("Server msg:",msg.decode())

sockfd.close()
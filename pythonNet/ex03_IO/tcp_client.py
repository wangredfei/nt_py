from socket import *


# 发起链接
sockfd = socket()
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)
# 消息收发
while 1 :
    data = input(">>>")
    if not data :
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server:", data.decode())
    
sockfd.close()
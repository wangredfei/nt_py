from socket import *


# 发起链接
while 1 :
    sockfd = socket()
    server_addr = ('127.0.0.1',9999)
    sockfd.connect(server_addr)
    # 消息收发
    data = input(">>>")
    sockfd.send(data.encode())
    if data == 'q':
        break
    data = sockfd.recv(1024)
    print("From server:", data.decode())
    
sockfd.close()
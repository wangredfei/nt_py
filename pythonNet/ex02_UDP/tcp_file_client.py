from socket import *


# 发起链接
s = socket()
server_addr = ('0.0.0.0',9999)
s.connect(server_addr)
a = open('timg.jpeg',"rb")
# 消息收发
while 1 :
    data = a.read(4098)
    if not data :
        break
    s.send(data)

    
a.close()
s.close()
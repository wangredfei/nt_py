from socket import *
s = socket(AF_INET,SOCK_DGRAM)

# 设置可以接受广播
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('0.0.0.0',9898))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("mag:",msg.decode())
    except KeyboardInterrupt:
        break

s.close()

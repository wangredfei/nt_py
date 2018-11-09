from socket import * 
from time import sleep

# 设置一下广播地址
dest = ("192.168.43.255",9898)
s = socket(AF_INET,SOCK_DGRAM)

# 设置可以广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("baby ".encode(),dest)
s.close()
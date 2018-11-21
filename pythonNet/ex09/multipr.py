from multiprocessing import Process
from socket import *
import sys,time

def handel():
    time.sleep(2)
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data :
            break
        print(data.decode())
        c.send(b'Recive')
    c.close()
    sys.exit(0)# 退出子进程

HOST = ('0.0.0.0')
PORT = 8888
ADDR = (HOST,PORT)

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 进入主循环
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("客户端退出")
    except Exception as e:
        print(e)
        continue
    
    # 创建多进程
    p = Process(target=handel)
    p.daemon = True 
    p.start()
    ??????????????
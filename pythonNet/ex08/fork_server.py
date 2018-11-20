from socket import * 
import os,sys

def client_handle(c):
    print("客户端: ",c.getpeername())
    while True: 
        data = c.recv(1024)
        if not data :
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()


# 创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
s = socket() # tcp 套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 循环等待客户端链接
print("wait......")
while True: 
    try : 
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    # 创建新的进程处理客户端请求
    pid = os.fork()
    if pid < 0 :
        pass
    elif pid == 0:
        # 创建二级子进程
        p = os.fork()
        if p == 0:

            s.close()
            # 处理具体的客户端请求
            client_handle(c) 
            # 客户端处理完毕子进程退出
            os._exit(0) 
        else :
            os._exit(0)
    else :
        c.close()
        os.wait()
        continue

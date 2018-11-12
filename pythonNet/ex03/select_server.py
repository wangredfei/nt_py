from select import select
from socket import *

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0",9999))
s.listen(5)


# 添加到关注列表
rlist = [s]
wlist = []
xlist = []

while 1:
    # 循环监控IO事件的发生
    rs, ws, xs = select(rlist, wlist, xlist)    

    # 处理发生的IO事件

    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data :
                rlist.remove(r) # 客户端退出,移除关注
                r.close()
                continue
            print("收到:",data.decode())
            # r.send(b"Recive")
            wlist.append(r)
    for w in ws:
        w.send(b'Receive')
        wlist.remove(w)
    for x in xs:
        pass
# coding=utf-8
''' 
chat room 
env:python3
socket and fork
'''
from socket import *
import os

def do_login(s, user, name, addr):
    if (name in user) or name == "管理员":
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr)
    msg = "欢迎 %s 加入聊天室" % name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr

def do_chat(s,user,name,text):
    line = "%s 说 %s"%(name, text)
    for i in user:
        if i != name:
            s.sendto(line.encode(),user[i])

def do_quit(s, user, name):
    msg = "%s 退出了聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[name])
    del user[name]

def do_request(s):
    # 存储用户 {"zhangsan":('127.0.0.1',8888)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(" ")
        print(msgList)
        # 区分请求类型
        if msgList[0] == "L":
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == "C":
            # 重新组织消息
            text = " ".join(msgList[2:])
            do_chat(s,user,msgList[1],text)
        elif msgList[0] == "Q":
            
            do_quit(s, user,msgList[1])



def main():
    # 创建UDP套接字
    ADDR = ('0.0.0.0',8888)
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    pid = os.fork()
    if pid < 0 :
        print("Create process failed")
        return
    
    # 子进程发送管理员消息
    elif pid == 0:
        
        msg = input("管理员消息:")
        msg = "C 管理员 %s"%msg
        s.sendto(msg.encode(),ADDR)
    # 父进程处理客户端请求
    else :
        do_request(s)

if __name__ == "__main__":
    main()
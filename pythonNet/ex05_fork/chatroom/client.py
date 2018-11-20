from socket import *
import os,sys

def send_msg(s , name , ADDR):
    while True:
        try:
            text = input("发言: ")
        except KeyboardInterrupt:
            text = "quit"
        if text == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"% (name,text)
        s.sendto(msg.encode(),ADDR)
        
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(1024)
        if data.decode() == "EXIT":
            os._exit(0)
        print(data.decode()+"\n发言: ",end="")
        

def main():
    if len(sys.argv) < 3:
        print("argv is error!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    # 创建UDP套接字
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        user_name = input("Please input your name: ")
        # 为了区别发送名字和发送内容
        msg = "L "+ user_name
        s.sendto(msg.encode(),ADDR)
        # 接受反馈
        data ,addr = s.recvfrom(1024)
        if data.decode() =='OK':
            print("您已经进入聊天室")
            break
        else :
            print(data.decode())
            continue
    # 创建收发进程
    pid = os.fork()
    if pid < 0 :
        print("Create process error")
    elif pid == 0:
        recv_msg(s)
    else:
        send_msg(s,user_name,ADDR)
if __name__ == "__main__":
    main()
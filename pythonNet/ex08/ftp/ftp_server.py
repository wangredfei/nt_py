from socket import * 
from threading import Thread
import os 
import sys
import time 


class FtpServer():
    '''这是一个文件类'''
    def __init__(self,c):
        self.c = c
    
    def do_list(self):
        file_list = os.listdir(FILE_DIR)
        if not file_list:
            self.c.send("文件库为空".encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.05)
        for file in file_list:
            if file[0] != "." and os.path.isfile(FILE_DIR + file):
                self.c.send(file.encode())
                time.sleep(0.05)
        self.c.send("##".encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_DIR+filename,"rb")
        except :
            self.c.send("文件不存在".encode())
            return
        else :
            self.c.send(b'OK')
            time.sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data :
                time.sleep(0.1)# 防止粘包
                self.c.send(b"##")
                break
            self.c.send(data)
        fd.close()

    def do_put(self,filename):
        try:
            fd = open(FILE_DIR+filename,"wb")
        except:
            self.connfd.send("上传失败")
        else:
            self.c.send(b"OK")
            time.sleep(0.1)
        while True:
            data = self.c.recv(1024)
            if  data == b"##":
                break
            fd.write(data)
        fd.close()
        print("%s上传完成"% filename)




FILE_DIR = '/home/tarena/nt_py/pythonNet/ex08/ftp/a/'
def zombie():
    os.wait()     
        
def main():    
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',8888))
    s.listen(5)

    print('wait')
    while True:
        try :
            c, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue
        print("链接用户:",addr)
        pid = os.fork()
        
        if pid == 0:
            s.close()
            ftp = FtpServer(c)
            while True:
                data = c.recv(1024).decode()
                if data[0] == "Q" or not data:
                    c.close()
                    sys.exit("客户端退出")
                elif data[0] == "L":
                    ftp.do_list()
                elif data[0] == "G":
                    filename = data.split(" ")[-1]
                    ftp.do_get(filename)
                elif data[0] == "P":
                    filename = data.split(" ")[-1]
                    ftp.do_put(filename)
            os._exit(0)            
        else: 
            c.close()
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue

main()
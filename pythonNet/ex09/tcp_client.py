from socket import *
import sys
import time


# 具体功能实现
class FtpClient(object):
    def __init__(self,s):
        self.s = s
    
    def do_list(self):
        self.s.send(b"L")
        data= self.s.recv(1024).decode()
        if data == "OK":
           
            while True:
                file = self.s.recv(1024).decode()
                if file  == "##":
                    break
                print(file)
                            
        else:
            # 无法操作
            print(data)

    def do_quit(self):
        self.s.send(b'Q')
        self.s.close()
        sys.exit("谢谢使用")

    def do_get(self, filename):
        self.s.send(('G '+filename).encode())
        data = self.s.recv(1024).decode()
        if data == "OK":
            fd = open(filename, "wb")
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s下载完成"%filename)
        else :
            print(data)

    def do_put(self,filename):
        try :
            f = open(filename,"rb")
        except:
            print("没有该文件")
            return
        
        self.s.send(('P '+filename).encode())
        data = self.s.recv(128).decode()
        if data == "OK":
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)
            f.close()
            print("%s文件上传完毕"%filename)

        else:
            print(data)



# 网络链接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = sys.argv[2]
    ADDR = (HOST,int(PORT))
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("链接服务器失败: ",e)
        return
    # 创建类对象
    ftp = FtpClient(s)

    while True:
        print("======命令选项=======")
        print('***    list     ***')
        print('***  get list   ***')
        print('***  put list   ***')
        print('***    quit     ***')
        print("====================")

        cmd = input("输入命令:")
        
        if cmd.strip() == 'list':
            ftp.do_list()

        elif cmd.strip() == "quit":
            ftp.do_quit()

        elif cmd[:3] == "get":
            filename = cmd.strip().split(" ")[-1]
            ftp.do_get(filename)
            
        elif cmd[:3] == "put":
            filename = cmd.strip().split(" ")[-1]
            ftp.do_put(filename)

        else :
            print("请输入正确命令")


main()
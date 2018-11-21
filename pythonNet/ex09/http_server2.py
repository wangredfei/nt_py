# coding = utf-8
''' 
HTTP SERVER v2.0
解析具体request
使用多线程并发处理
能返回简单数据
使用类封装
'''

from socket import *
from threading import Thread
import sys

# 封装httpserver 功能
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        
        # 创建套接字
        self.create_socket()

    def create_socket(self):
        '''用于创建套接字'''
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)
        

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen to the port",self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print(e)
                continue

            # 创建线程处理客户端请求
            clinetThread = Thread(target=self.handle,args=(connfd,))
            clinetThread.setDaemon(True)
            clinetThread.start()
        
    # 处理客户端请求
    def handle(self,connfd):
        # 接受request
        request = connfd.recv(4096)
        requestHeaders = request.decode().splitlines()
        # print(connfd.getpeername(),":",requestHeaders[0])
        # 切割
        get_request = requestHeaders[0].split(" ")[1]
        # print(get_request)
        
        # 获取文件
        if get_request == "/" or get_request[-5:]==".html":
            self.get_html(connfd,get_request)
        
        # 获取数据
        else:
            self.get_data(connfd,get_request)

        connfd.close()

    def get_html(self,connfd,get_request):
        # 判断是否是主界面
        if get_request == "/":
            get_request = "index1.html"
        # 打开文件
        try:
            print(static_dir+"/"+get_request)
            fd = open(static_dir+"/"+get_request, "r")
        # 如果请求不到,返回404
        except Exception as e:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            response += "<h1>Not Found!!!</h1>"
        # 否则返回
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            while True:
                data = fd.read(4096)
                if not data:
                    break
                response += data
            fd.close()
        # 最后发送
        finally:
            connfd.send(response.encode())


    def get_data(self,connfd,get_request):
        urls = ['/time','/web','/python']
        if get_request in urls:
            if get_request == "/time":
                import time 
                responseBody = time.ctime()
            elif get_request == "/web":
                responseBody = "Wob Frame"
            elif get_request == "/python":
                responseBody = "Python"
            
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
        else:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseHeaders +="<h1>NONE</h1>"
        response = responseHeaders + responseBody
        connfd.send(response.encode())
        

# 提供服务器地址和静态文件路径
server_addr = ('0.0.0.0', 8000)
static_dir = "/home/tarena/nt_py/pythonNet/ex09/static"
httpd = HTTPServer(server_addr,static_dir)
# 调用函数启动服务
httpd.serve_forever()
from socketserver import *


# 创建服务器类
class Server(ForkingMixIn,TCPServer):
    pass

# 处理请求类
class Handle(StreamRequestHandler):
    # 重写父类方法
    def handle(self):
        print("Connect from: ",self.client_address)# 相当于链接套接字
        while True:
            # self.request ==> accept 返回链接的套接字
            data = self.request.recv(1024)
            if not data :
                break
            print(data.decode())
            self.request.send(b'Receive')

server = Server(('0.0.0.0',8778),Handle)
server.serve_forever() # 启动服务

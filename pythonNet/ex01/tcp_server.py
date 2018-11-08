import socket

# 创建套接字
sockfd = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)
# 绑定地址
sockfd.bind(('127.0.0.1',8588))

# 设定监听
sockfd.listen(5)

print("Waiting for connect .. .")

# 处理客户端连接
connfd,addr = sockfd.accept()

print(connfd, "-------",addr)

# 收发消息
data = connfd.recv(1024)
print("Receive: ",data)

n = connfd.send("Hello world!".encode())

print("Send %d bytes"%n)

connfd.close()
sockfd.close()
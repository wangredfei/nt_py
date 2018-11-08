import socket

# 创建套接字
sockfd = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)
# 绑定地址
sockfd.bind(('0.0.0.0',6666))
while 1 :

    # 设定监听
    sockfd.listen(5)

    print("Waiting for connect .. .")

    # 处理客户端连接
    connfd,addr = sockfd.accept()

    print("-------",addr)

    # 收发消息
    data = connfd.recv(1024)
    print(data)
    if data == b'q':
        break
    n = connfd.send("Hello world!".encode())

    print("Send %d bytes"%n)
    
    

connfd.close()
sockfd.close()
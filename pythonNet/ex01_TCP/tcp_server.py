import socket

# 创建套接字
sockfd = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)
# 绑定地址
sockfd.bind(('0.0.0.0',8866))

# 设定监听
sockfd.listen(5)


while 1 :
    print("Waiting for connect .. .")
    # 处理客户端连接
    try:
        connfd,addr = sockfd.accept()
        print("-------",addr)
    except KeyboardInterrupt:
        break
    while True:
        # 收发消息
        data = connfd.recv(1024)
        # 如果通道关闭,直接返回空字符串
        if not data :
            break
        print(data)
        n = connfd.send("Hello world!".encode())

        print("Send %d bytes"%n)
    connfd.close()
        
    

sockfd.close()
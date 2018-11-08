import socket

sockfd = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)

# 绑定服务器
sockfd.bind(("0.0.0.0",9999))

while 1: 
    sockfd.listen(2)
    print("wait to connect....")
    connfd, addr = sockfd.accept()
    data = connfd.recv(1024)
    print(data)
    if data == b"q":
        break
    n = connfd.send("nihao".encode())
    print("zijieshu = ", n)

connfd.close()
sockfd.close()

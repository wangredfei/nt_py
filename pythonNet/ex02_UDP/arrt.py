from socket import *
sockfd = socket()
# 设置端口重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(("127.0.0.1",8888))
print(sockfd.fileno())
sockfd.listen(5)
s,addr = sockfd.accept()

print(s.getpeername())
s.recv(1023)
# 获取选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
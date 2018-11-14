from socket import *
import struct

# 创建一个数据报套接字 
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

# 定义一个接受数据格式
# st = struct.Struct('i20sf')

while True:
    data,addr = s.recvfrom(1024)
    # 按照格式转换
    fmt = data.decode()
    data2,addr = s.recvfrom(1024)
    data2 = struct.unpack(fmt, data2)
    print(data2)

s.close() 

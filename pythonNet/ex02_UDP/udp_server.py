from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)


sockfd.bind(("0.0.0.0",9999))

while True:
    print("waiting....")
    data,addr = sockfd.recvfrom(1024)
    print("Receive from", addr, data.decode())
    sockfd.sendto(b'Thanks for you massage',addr)

sockfd.close()
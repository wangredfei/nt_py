from socket import *

s = socket()

s.bind(('0.0.0.0',8898))
s.listen(5)
f = open("aaa.html","r")
respond='''HTTP/1.1 200 OK
    Content_Encoding:gzip
    content_Type:text/html

    '''
for i in f:
    respond+=i


while 1 :
    c,addr = s.accept()
    a = c.recv(5555)

    c.send(respond.encode())
    c.close()
s.close()
f.close()


'''???
from socket import *
sockfd = socket()
sockfd.bind(("0.0.0.0",3544))
f = open("bbb.html","rb")

sockfd.listen(5)
print("wait....")
while 1:
    connfd, addr = sockfd.accept()
    a = connfd.recv(4098)
    data = f.read()
    connfd.send(data)
connfd.close()
f.close()
sockfd.close()
'''
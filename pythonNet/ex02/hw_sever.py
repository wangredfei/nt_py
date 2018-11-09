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

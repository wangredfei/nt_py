from socket import *

s = socket()

s.bind(('0.0.0.0',9999))
s.listen(15)

print("wait...")
f = open("Newfile.jpeg","wb")
c, addr = s.accept()
while 1:
    file_data = c.recv(4098)
    if not file_data:
        break
    f.write(file_data)

    


f.close()
c.close()
s.close()

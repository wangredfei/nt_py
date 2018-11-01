f = open("lx1_info.txt","rb")

b2 = f.read()

print(b2)
f.close()
s = b2.decode('utf-8')
print(s)
import os,time

filename = "./timg.jpeg"

# 获取文件大小
size = os.path.getsize(filename)
f = open(filename,'rb')

# 上半部分

def copy1():
    # f = open(filename,'rb')
    fw = open('1.jpg', 'wb')
    n = size//2
    # 因为f在外部打开,所以父进程读完后应将指针归0
    f.seek(0)
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

def copy2():
    # f = open(filename,'rb')
    fw = open('2.jpg','wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data :
            break
        fw.write(data)
    f.close()
    fw.close()

pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    time.sleep(2)
    copy1()
else :
    copy2()
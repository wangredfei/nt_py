# 此示例示意用随机定位的方式读取lx5_myfile.txt文件中的内容
try:
    f = open("lx5_myfile2.txt","rb")
    print("新打开的文件的读写位置是:",f.tell())
    b = f.read(2)
    print("读两个字节后的文件读写位置是",f.tell())
    f.seek(5,1)
    b2 = f.read(5)
    print("我读取的内容是",b)
    print("我读取的内容是",b2)
except OSError:
    print("打印文件失败")

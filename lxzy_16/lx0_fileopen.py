# 1. 打开文件
#   1). 相对路径
# myf = open("lx0_newfile1.py")
#   2). 绝对路径
filename = '/home/tarena/nt_py/lxzy_16/lx0_newfile1.txt'
myf = open(filename)
print("文件打开成功")
# 2. 读/写文件
line1 = myf.readline()
print("此行长度是:%d,内容是:\n"% (len(line1))+line1)
line2 = myf.readline()
print("此行长度是:%d,内容是:\n"% (len(line2))+line2)
line3 = myf.readline()
print("此行长度是:%d,内容是:\n"% (len(line3))+line3)
line4 = myf.readline()
if line4 =="":
    print('已经到行尾了')
# 3. 关闭文件
myf.close()
print("文件已经关闭")
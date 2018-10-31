'''
迭代器
it  = iter("123123")
print(it)
print(next(it))
print(next(it))
print("-"*50)
for i in it :
    print(i)
'''
'''
a = range(19)
print(next(iter(a)))
print(next(iter(a)))
print(next(iter(a)))
print(next(iter(a)))
print(next(iter(a)))
'''
'''
a = [1,2,3,4,5,6,7]
b = ['a','b','c','d', 'e','f','g']
for i in zip(a,b,range(10)):
    print(i)
c = dict(zip(a,b))
print(c)
'''
# a = [1,2,3,4,5,6,7]
# b = ['a','b','c','d', 'e','f','g']
# for i in enumerate(b,start = 65):
#     print(i)
'''
def A():
    a = 1
    while a<5:
        yield a**2+1
        a+=1
for i in iter(A()):
    print(i)
a = A()
print(a)
b = (x*5 for x in range(18))
for i in b:
    print(i)
'''
# l = [1,2,3,4,5,6,7]
# c = (x*5 for x in l)
# for i in c:
#     print(i)
# print("-"*5)
# l[3] = 44
# for i in c:
#     print(i)

# file_read_binary.py

# 此示例示意用二进制文件操作来读取文本文
# 件里的内容
'''
try:
    f = open('myfile.txt', 'rb')
    b = f.read(5)  # b绑定字节串
    print(b)
    print("字节串的长度是:", len(b))
    b2 = f.read()
    print(b2)
    print("字节串b2的长度是:", len(b2))

    b3 = f.read()  # b3 绑定空字节串
    print(b3 == b'')  # True
    f.close()
    # 将b2的内容转为字符串打印:
    s = b2.decode('utf-8')
    print(s)
    print("字符串s的长度是:", len(s))

except OSError:
    print("打开读文件失败!")
'''
# seek.py

# 此示例示意用随机定位的方式读取myfile2.txt文件中的内容
'''
try:
    f = open('myfile2.txt', 'rb')
    print("新打开的文件的读写位置是:", f.tell()) # 0

    b = f.read(2)  # 读取两个字节后
    print("读两个字节后的文件读写位置是:", f.tell())
    print("读取的内容是:", b)

    # 以下用seek方法让读写位置定位到5的位置
    # f.seek(5, 0)  # 从文件头向后5个字节
    # f.seek(3, 1)  # 从当前位置向后移动3个字节
    f.seek(-15, 2)  # 从文件尾前移动15个字节


    print("移动的后位置是:", f.tell())  # 5
    b2 = f.read(5)
    print("b2=", b2)  # b'abcde'
    f.close()
except OSError:
    print("打开文件失败")
'''
'''
f = open("aaa.py","w")
f.write("nihao")
f.flush()
input()
'''

# class Dog():
#     pass
# dog1 = Dog()
# dog1.color = "bai"
# dog1.__dict__['kdis'] = 'jingba'
# print(dog1.__dict__)


# n = int(input("请输入"))
# raise StopIteration

'''
class MyList:
    def __init__(self,iterable):
        self.date = [x for x in iterable]
    def __repr__(self):
        return "Mylist(%s)"%self.date
    def __neg__(self):
        a = [-x for x in self.date]
        return MyList(a)
class A(MyList,object):
    pass
l = [1,-2,3,-4]
ll = MyList(l)
l2 = -ll
print(l2)
print(A.__bases__)
'''

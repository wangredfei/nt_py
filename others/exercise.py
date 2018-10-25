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
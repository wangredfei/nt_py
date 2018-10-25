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
l = [1,2,3,4,5,6,7]
c = (x*5 for x in l)
for i in c:
    print(i)
print("-"*5)
l[3] = 44
for i in c:
    print(i)

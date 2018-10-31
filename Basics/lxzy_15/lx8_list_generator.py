l = [2,3,5,7]
a = [x*10 for x in l] # 生成一个新的列表a
it = iter(a)
print(next(it))# 20
l[1] = 333  # 改变了原来的列表,但是不改变新的列表
print(next(it))# 30


l = [2,3,5,7]
a = (x*10 for x in l)  # a  中只有推导式没有数据 ,需要向列表要数据
it = iter(a)
print(next(it))# 20
l[1] = 333  
print(next(it))# 3330


l = [1,2,3,4,5,6,7]
c = (x*5 for x in l)
for i in c:
    print(i)
print("-"*5)
# 下面遍历不会被打印,因为生成器只能生成一次
l[3] = 44
for i in c:
    print(i)

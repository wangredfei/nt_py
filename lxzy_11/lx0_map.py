# def power2(x, y):

#     print("被调用")
#     return x*y

# for x in map(power2,range(1,10),range(10, 1,-1)):
#     print(x)


for y in map(pow,range(1,6),range(6,11),range(11,16)):
    print(y)

# 当函数从任意一个迭代对象取不到值时,则结束
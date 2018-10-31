def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("即将生成9")
    yield 9
    print("生成结束")
r = myyield() # r 绑定的是生成器
for x in r:
    print(x)
print('----')
# 生成器对象是一次性的,一旦生成结束以后,将不能再重新生成数据
for x in r:
    print(x)
print("-----")
for x in myyield():
    print(x)
print("-----")
for x in myyield():
    print(x)
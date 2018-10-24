# 此示例示意用生成器函数制造一个整数序列生成器
# 此生成器能生成从0 开始到n的整数(不包含n)
def myinteger(n):
    i = 0
    while i< n :
        yield i
        i += 1
for x in myinteger(3):
    print(x)
l = [x for x in myinteger(100)]
print(l)
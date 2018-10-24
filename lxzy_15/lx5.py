l = [2,3,5,7]
# 函数
def myfun(l):
    for x in l:
        yield x**2+1
# 表达式
gen = (x**2+1 for x in l)
# 列表
ll = list(x**2+1 for x in l)
# 结果
for i in myfun(l):
    print(i)
print(gen)
print("-"*10)
for j in gen:
    print(j)
print("-"*10)
print(ll)
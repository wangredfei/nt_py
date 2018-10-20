
#   2. 给出一个数n,写一个函数myfac来计算n!(n的阶乘)
#     n! = 1 * 2 * 3 * ... * n
# print(myfac(5))  # 120
def myfac(n):
    N = 1
    for i in range(1,n+1):
        N *= i
    return N
print(myfac(5))
#   ３．　编写函数fun,其实能是计算下列多项式的和
#      Sn = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
#      建义用数学模块里的factorial
#      求n 等于500时的值
def fun(n):
    import math
    Sn = 0
    if n == 0:
        return 1
    k = 1/math.factorial(n)
    Sn = k+ fun(n-1)
    return Sn
print(fun(500))
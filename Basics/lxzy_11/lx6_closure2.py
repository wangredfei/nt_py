# 用闭包来创建一元二次方程的函数


def get_fx(a,b,c):
    def fx(x):
        return a*x**2+b*x+c
    return fx
# 得到函数x**2+2*x+3
f123 = get_fx(1,2,3)
print(f123(50))
print(f123(20))

f456 = get_fx(4,5,6)
print(f456(50))

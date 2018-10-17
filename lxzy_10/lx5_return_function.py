def f1():
    print("f1")
def f2():
    print("f2")
def get_fx(n):
    if n == 1:
        return f1
    if n == 2:
        return f2
fx = get_fx(1)
fx()# 运行f1
fx = get_fx(2)
fx()# 运行f2

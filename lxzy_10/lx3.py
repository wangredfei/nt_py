def f1():
    print("f1 is begin")
def f2():
    print("f2 is begin")
def fn(fs):
    print(fs)
    fs()
    fs()
fn(f1)# 函数并没有调用
f2()
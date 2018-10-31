def f1():
    print("f1 is begin")
def f2():
    print("f2 is begin")    
f1, f2 = f2, f1
# 交换
f1()
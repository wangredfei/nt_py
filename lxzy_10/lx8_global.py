# # global 语句的语法和用法
# v = 100
# def f1():
#     global v 
#     # 生命v时全局变量
#     v = 200
# f1()
# print("v = " ,v )
c = 100
def A():
    c=50
    print(c)
    def B():
        nonlocal c
        c = 25
        print(c)
    B()
    print(c)
A()
print("quanjv", c)
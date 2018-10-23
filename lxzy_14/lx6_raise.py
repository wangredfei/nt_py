'''
def make_except():
    print("开始")
    raise ValueError("afdsaf asdfsad")# 这是故意制造的错误
    # 相当于创建了一个对象,比如一封信 ,用raise扔出去,可以用err接受 
    # raise ZeroDivisionError("自定义的除零操作")
    print("结束")
try: 
    make_except()
except ValueError as err:
    print("得到make)except 里发出的异常通知",err)
print("程序结束")
'''
def f1(x):
    print(x)
    # 此处对x进行处理, 可能触发错误
    raise ValueError(str(x)+"此数值不能被处理")
def f2(x, y):
    try:
        f1(x)
    except ValueError as err:
        #只要被捕获就不会再次返回异常
        print("异常已经被处理")
        raise err # 除非再次发送异常　或者写ｒａｉｓｅ 不加err
    print(x,y)
try:# 不会再次返回异常
    f2(0,100)
except ValueError as err:
    print("f2f2f2f2f2f2")
# f2(0,100)
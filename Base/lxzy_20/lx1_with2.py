# 示意将自定义的类变为环境管理器
# 让自定义的类创建的对象能用在with语句中
class A():
    def __enter__(self):
        print("A类对象已经进入with语句")
        return self # 比如return 否则a绑定的就是None
    def __exit__(self, e_type, e_value, e_tb):
        '''
        e_type 绑定的是异常类型,没有异常返回None
        e_value 绑定错误对象,没有异常返回None
        e_tb 绑定追踪对象,没有异常返回None
        '''
        if e_type is None:
            print("我是没有异常时退出的with语句")
        else:
            print("有异常发生")
            print(e_type)
        print("A类对象已离开with语句")
with A() as a :
    print("这是with语句内部的一条语句")
    int(input("aaa:"))
print("程序正常退出")
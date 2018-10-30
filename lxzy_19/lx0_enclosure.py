# 此示意示意用私有实例变量和私有属性来演示封装
class A():
    def __init__(self):
        self.__ppp = 100 # 创建私有属性
        self.ppp = 200 # 非私有属性
    def __test(self):
        print("私有属性__test属性的值为",self.ppp)
    def test(self):
        self.__test()# 内部可以调用
        print("__ppp属性的值为",self.ppp)
a = A()
# print(a.__PPP)
print(a.ppp)
# a.__test()# 出错
a.test()
print(a._A__test())
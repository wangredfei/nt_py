# mynumber.py


# 此示例示意让自定义的类能够使用内建函数进行操作
class Number:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print('__str__被调用')
        return "数字: %d" % self.data

    def __repr__(self):
        print("__repr__被调用")
        return 'Number(%d)' % self.data

n1 = Number(100)

print("repr(n1)=", repr(n1))  #n1.__repr__()
print("str(n1)= ", str(n1))  #n1.__str__()
print(n1)  # n1.__str__()
# n2 = Number(200)



# mynumber2.py


# 此示例示意int, float函数的重写方法

class MyNumber:
    def __init__(self, value):
        self.data = value

    def __int__(self):
        '''此方法用于将对象self.转为整数
        此方法必须返回整数
        '''
        return int(self.data)

n1 = MyNumber("100")
print(int(n1))  # 调用n1.__int__()
# print(float(n1))  # 调用n1.__float__()
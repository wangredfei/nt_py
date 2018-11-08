class MyNumber():
    def __init__(self, value):
        self.date = value
    def __int__(self):
        '''此方法用于将对象self.转为整数,必须返回整数'''
        return int(self.date)
    def __float__(self):
        '''此方法必须返回浮点数'''
        return float(self.date)
    
n1 = MyNumber(100)
print(int(n1))
print(float(n1))
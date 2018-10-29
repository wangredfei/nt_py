class A:
    v = 100 # 类变量
    @classmethod
    def get_v(cls):
        '''这是一个类方法用来获取类变量v的值'''
        return cls.v
    @classmethod
    def set_v(cls,value):
        cls.v = value
    

print(A.get_v()) # 获取类变量v的值
A.set_v(200)
print(A.get_v()) 

class Human:
    # 让HUman创建的对象只允许有name 和age 属性
    __slots__ = ['name','age']
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def show_info(self):
        print(self.name,self.age)
h1 = Human("tarena",15)
h1.show_info()
h1.age = 16
h1.Age = 16# 会报错,因为此属性不在slots列表内
h1.show_info()
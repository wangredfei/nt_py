#此示例示意ｄｅｌ语句析构方法
class Car():
    def __init__ (self,info):
        self.info = info
        print("Car",info,"is created")
    def __del__(self):
        print("汽车",self.info,'对象即将销毁')

c1 = Car("BYD E6")
# c2 = c1
# del c1  
input("输入回车键继续 : ")
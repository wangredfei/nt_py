# 此实例示意实例属性的创建及使用

class Dog():

    def eat(self,food):
        print(id(self),"的小狗在吃",food)
    def sleep(self,hour):
        print("小狗睡了",hour,"小时")
    def play(self,obj):
        print(id(self),"的小狗在玩",obj)
    
dog1 = Dog()
dog1.color ='白色'
dog1.kinds ='京巴'
print(dir(dog1))
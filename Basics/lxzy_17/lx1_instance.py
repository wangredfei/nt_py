# 此示例示意在类内定义实例方法的语法和调用语法
class Dog():

    def eat(self,food):
        print(id(self),"的小狗在吃",food)
    def sleep(self,hour):
        print("小狗睡了",hour,"小时")
    def play(self,obj):
        print(id(self),"的小狗在玩",obj)
        
dog1 = Dog()# 创建一个对象
dog1.eat("屎")
dog1.sleep(3)
dog1.play("ball")

dog2 = Dog()# 创建一个对象
dog2.eat("狗粮")
dog2.sleep(5)
dog2.play("frisbee")

# 以下示意用类名来调用实例方法

Dog.eat(dog1,"包子")
Dog.eat(dog2,"饺子")
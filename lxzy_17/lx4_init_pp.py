class Human :
    def __init__(self,name,age,address="None"):
        self.name = name
        self.age = age
        self.address = address
    def show_info(self):
        print(self.name , '今年' , self.age , "岁,家住",self.address)
    def run(self,speed):
        print(self.name ,"is running by ",speed, "km/h ")

s1 = Human("小张",20,'北京市东城区')
s2 = Human("小李",18)
s1.show_info()
s2.show_info()
s1.run(50)


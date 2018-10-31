class Human :
    '''定义一个人'''
    def set_info(self,name,age,address="None"):
        self.name = name
        self.age = age
        self.address = address
    def show_info(self):
        print(self.name , '今年' , self.age , "岁,家住",self.address)


s1 = Human()
s1.set_info("小张",20,'北京市东城区')
s2 = Human()
s2.set_info("小李",18)
s1.show_info()
s2.show_info()
print(s1.__doc__)
print(s1.__dict__)
print(dir(s1))
print(s1.__dir__)
print(s1.__class__)
print(s1.__init__)
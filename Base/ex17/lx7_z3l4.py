# 1.   有两个人:  第一个人: 姓名:张三 , 年龄 :35岁:  第二个人: 姓名:李四 , 年龄 :15岁
#     1. 行为:
#         1. 教别人学东西 teach
#         2. 工作赚钱 work
#         3. 借钱 borrow
#         4. 显示自己的信息 show_info
#     2. 事情
#         - 张三教李四学python
#         - 李四教张三学王者荣耀
#         - 张三上班赚了1000元
#         - 李四向张三借钱200元
#         - 35岁的张三有钱800元,他学会的技能是王者荣耀
#         - 15岁的李四有钱200元,他学会了python
class Human():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        self.money = 0
        self.skill = []
    def teach(self,other,skill):
        other.skill.append(skill)
        print(self.name ,'教', other.name ,'学',skill)
    def work(self,money):
        self.money += money
        print(self.name , "上班挣了",money, "元")
    def borrow(self,other,money):
        if other.money < money:
            print("她没有那么多钱,他现在只有",other.money)
            print("借钱失败")          
            return
        self.money += money 
        other.money -= money
        print("{}向{}借了{}元".format(self.name,other.name,money))
    def show_info(self):
        print("{1}岁的{0}有钱{2}元,他学会的技能是{3}".format(self.name,self.age,self.money,"".join(self.skill)))

zh3 = Human("张三",35)
li4 = Human("李四",15)

zh3.teach(li4,"python")
li4.teach(zh3,"王者荣耀")
zh3.work(1000)
li4.borrow(zh3,200)
li4.borrow(zh3,200)
li4.borrow(zh3,200)
li4.borrow(zh3,200)
li4.borrow(zh3,200)
li4.borrow(zh3,200)
zh3.show_info()
li4.show_info()
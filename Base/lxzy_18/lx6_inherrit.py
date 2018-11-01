class Human:
    def say(self,what):
        print("说:",what)
    def walk(self,distance):
        print("走了",distance,'公里')
h1 = Human()
h1.say("天凉了!")
h1.walk(5)
class Student(Human):
    def study(self,subject):
        print("学习:",subject)
s1 = Student()
s1.study("python")
s1.walk(20)
s1.say("你是个大猪蹄子")
class Teacher(Student,Human):
    def teach(sefl,subjict):
        print("在教",subjict)
t = Teacher()
t.study("aaa")
t.say('asdfa')
print(Teacher.__base__)
     
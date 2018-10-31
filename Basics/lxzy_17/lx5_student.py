class Student():
    def __init__(self,name,age,score=0):
        self.name = name
        self.age = age
        self.score =score
        return
    def set_score(self,new_s):
        self.score = new_s
    def show_info(self):
        print("name:{},age:{},score:{}".format(self.name , self.age , self.score))
L = []
L.append(Student('小张',20,100))
L.append(Student('小李',18,95))
L.append(Student('小孔',18))
# print(L)
# L[-1].set_score(70)
# for s in L:
#     print(s.name)
print(L[0].name)
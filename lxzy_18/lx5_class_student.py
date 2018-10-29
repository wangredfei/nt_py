class Student():
    l = []
    def __init__(self , name , age , score):
        self.name = name
        self.age = age
        self.score = score
    # 添加学生类方法
    @classmethod
    def add_student(cls,name,age,score):
        cls.l.append(Student(name,age,score))
    # 删除学生类方法
    @classmethod
    def del_student(cls,dname):
        for ll in cls.l:
            if dname == ll.name:
                cls.l.remove(ll)
                print("删除成功")
                break
        else:
            print("don't have this person")
    # 学生个数
    @classmethod
    def p_count_st(cls):
        print("有%d个学生" % len(cls.l))
    # 学生平均年龄
    @classmethod
    def p_average_age(cls):
        sum_age = []
        for ll in cls.l:
            sum_age .append( ll.age)
        print("平均年龄为",sum(sum_age)/len(sum_age))
    # 学生平均成绩
    @classmethod
    def p_average_score(cls):
        sum_score = []
        for ll in cls.l:
            sum_score.append(ll.score)
        print("平均成绩为",sum(sum_score)/len(sum_score))
def main():
    while 1:
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.查看学生个数")
        print("4.获取学生平均年龄")
        print("5.获取学生平均成绩")
        print("q:退出")
        try:
            num = input("请输入您想要的操作")
        except:
            print("输入有误,请从新输入")
            continue
        if num == "1":
            while 1 :
                iname = input("name:")
                if not iname:
                    break
                try:
                    iage = int(input("age:"))
                    iscore = int(input("score:"))
                    Student.add_student(iname,iage,iscore)
                    print("添加成功")
                except:
                    print("请输入正确内容")
                    continue

        elif num == "2":
            dname = input("顺如想删除谁的信息")
            Student.del_student(dname)
        elif num == "3":
            Student.p_count_st()
        elif num == "4":
            Student.p_average_age()
            print("successful")
        elif num == "5":
            Student.p_average_score()
            print("successful")
        elif num == "q":
            break
        else :
            print('没有该选项请从新输入')    
        print("-"*50)
        for ll in Student.l:
            print("{},{},{}".format(ll.name,ll.age,ll.score))
        print("-"*50)
if __name__ =="__main__":
    main()
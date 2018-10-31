# 此示例示意用特性属性虚拟一个score属性.
# 来对设置分数加以限制
class Student:
    def __init__(self, score=0):
        self.__score = score

    @property
    def score(self):
        print('''getter''')
        return self.__score

    @score.setter
    def score(self, v):
        print('''setter''')
        assert 0 <= v <= 100, "成绩超出范围"
        self.__score = v


s = Student()
print(s.score)  # 取值
s.score = 99    # 正确赋值
s.score = 10000  # 赋值报错
print(s.score)
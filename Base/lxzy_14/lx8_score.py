def get_score():
    s = int(input("请输入学生成绩: "))
    assert 0 <= s <= 100,'成绩超出范围'
    #等同于if bool(): raise AssertionError()
    return s
try:
    score = get_score()
    print("学生的成绩是",score)
except AssertionError as err:
    print(err)
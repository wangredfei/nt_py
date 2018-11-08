def get_score():
    try:
        n = float(input("请输入成绩(0-100):"))
    except ValueError:
        return 0
    if 0 <= n <= 100:
        return n
    return 0 
score = get_score()
print("学生成绩是：",score)

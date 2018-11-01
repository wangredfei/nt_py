# mymax = lambda x,y : x if x > y else y
# print(mymax(100, 200))


# lambda 赋值就是直接在后面加括号传实参
def fx(f, x, y):
    print(f(x, y))
fx((lambda a, b : a+b), 100, 200)
fx((lambda x, y : x**y), 3, 4)
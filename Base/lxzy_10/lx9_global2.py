# 用全局变量纪录一个函数hello的调用次数
count = 0
def hello(name):
    print("您好", name)
    global count 
    count += 1
hello("小张")
hello("小李")
print("hello 被调用了",count,'次')
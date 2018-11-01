# 1. 写一个程序，输入一个数，用if语句计算这个数的绝对值并打印出来
'''
number = int(input("请输入一个整数： "))
if number < 0 :
    print(-number)
elif number > 0 :
    print(number)
else :
    print("这是0")
'''



# 2. 写一个程序，输入一个数，用条件表达式计算这个数的绝对值并打印出结果

number = int(input("请输入一个整数： "))
s = -number if number < 0 else number+500 
print(s)
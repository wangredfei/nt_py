# 1. 写一个程序，输入一个数，用if语句计算这个数的绝对值并打印出来
'''
n = float(input("请输入一个数"))
if n > 0 :
    print(n)
elif n < 0:
    print(-n)
else :
    print("0")
'''


# 练习
# 4输入一个季度是1～4输出这个季度有哪几个月份。
# 如果输入的不是1～4的整数，提示用户您错哪里了
'''
n = int(input("请输入(1-4):"))
if n == 1:
    print("第1季度有:1,2,3月")
elif n == 2:
    print("第2季度有:4,5,6月")
elif n == 3:
    print("第3季度有:7,8,9月")
elif n == 4:
    print("第4季度有:10,11,12月")
else :
    print("输入有误,请输入(1-4")
'''
# 1. 北京出租记价器
# 收费标准：
    # 三公里以内收费13元
    # 基本单价 2.3元/公里（超出公里以外）
    # 空驶费：超过15公里后，每公里加收单价的50%的空驶费（3.45元/公里）
# 要求： 输入公里数，打印出费用金额
'''
km = float(input("请输入公里数"))
if  km <= 3:
    money = 13
elif km > 3 :
    money =13 + 2.3*(km-3)
elif km > 15 :
    money  = 13 + 12*2.3+(km-15)*3.45
else :
    print("输入有误")
print(money)
'''
# 2.输入一个学生的三科成绩：
    # 1.打印出最高分是多少分
    # 2.打印出最低分是多少分
    # 3.打印出平均分是多少分
'''
y = float(input("输入您的第一科成绩"))
s = float(input("输入您的第一科成绩"))
yy = float(input("输入您的第一科成绩"))
max_score = y
if max_score < s:
    max_score = s
elif max_score < yy:
    max_score = yy
min_score = y
if min_score > s:
    min_score = s
elif min_score > yy:
    min_score = yy
print("最大成绩",max_score)
print("最小成绩",min_score)
print("平均成绩",(y+s+yy)/3)
'''
# 3. 计算 BMI指数（Body Mass Index）又称身体质量指数
# 计算公式：
#   BMI = 体重（公斤）/身高的平方（米）
#     
# 如:一个69公斤的人，身高173公分，则
#     BMI = 69 / 1.73 ** 2  # 得23.05
# 标准表:
#     BMI < 18.5    体重过轻
#     18.5 <= BMI < 24  体重正常
#     BMI >= 24     体重过重
# 要求:  输入身高和体重，打印BMI的值，并打印体重状况
height = float(input("请输入您的身高"))
weigit = float(input("请输入您的体重"))
BMI = weigit/height**2
if BMI < 18.5 :
    print("体重过轻")
elif BMI < 24 :
    print("体重正常")
elif BMI >= 24:
    print("超重")

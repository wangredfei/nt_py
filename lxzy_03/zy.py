# 1. 北京出租记价器
# 收费标准：
    # 三公里以内收费13元
    # 基本单价 2.3元/公里（超出公里以外）
    # 空驶费：超过15公里后，每公里加收单价的50%的空驶费（3.45元/公里）
# 要求： 输入公里数，打印出费用金额
'''
l = float(input("公里数： "))
if 0 <= l <= 3 :
    print("您应支付13元")
elif 3 < l <= 15:
    money = 15 + (l - 3)*2.3
    print("您应支付%.2f" % money,"元")
elif l > 15:
    money = 13 + (15-3)*2.3 + (l-15)*3.45
    print("您应支付%.2f" % money)
else:
    print("您的输入有误，请从新输入")
'''
# 2.输入一个学生的三科成绩：
    # 1.打印出最高分是多少分
    # 2.打印出最低分是多少分
    # 3.打印出平均分是多少分
# 笨方法
'''
grade1 = int(input("第一科成绩： "))
grade2 = int(input("第二科成绩： "))
grade3 = int(input("第三科成绩： "))
# 最高分
if grade1 >= grade2 and grade1 >= grade3:
    print("最高分为",grade1)
elif grade2 >= grade1 and grade2 >= grade3:
    print("最高分为",grade2)
elif grade3 >= grade2 and grade3 >= grade1:
    print("最高分为",grade3)
# 最低分
if grade1 <= grade2 and grade1 <= grade3:
    print("最低分为",grade1)
elif grade2 <= grade1 and grade2 <= grade3:
    print("最低分为",grade2)
elif grade3 <= grade2 and grade3 <= grade1:
    print("最低分为",grade3)
average = (grade1 + grade2 + grade3)/3
print("平均分为%.2f"%average)
'''
# 函数
'''
grade1 = int(input("第一科成绩： "))
grade2 = int(input("第二科成绩： "))
grade3 = int(input("第三科成绩： "))
x_nu = max(grade1,grade2,grade3)
print("最高分为",x_nu)
n_nu = min(grade1,grade2,grade3)
print("最低分为",n_nu)
a_nu = (grade1 + grade2 + grade3) / 3
print("平均分为%.2f"%a_nu)
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
'''
height = float (input("请输入您的身高： "))
weigth = float (input("请输入您的体重： "))
BIM = weigth / height ** 2
if BIM < 18.5 :
    print("体重过轻")
elif 18.5 <= BIM < 24:
    print("体重正常")
elif BIM >= 24:
    print("体重正常")
'''
# 4. 写一个程序．打印一个高度为4行的矩形方框
# 要示方输入一个整数，此整数代表矩形的宽度，输入此矩形
# 如:
#     请输入矩形宽度: 10
# 打印如下:
#     ##########
#     #        #
#     #        #
#     ##########
# 如果输入的数字越大，则此矩形会越宽
d = int (input("宽度： "))
print("#"*d)
print("#"," "*(d-4),"#")
print("#"," "*(d-4),"#")
print("#"*d)


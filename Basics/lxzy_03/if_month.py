# 3.输入一年中的月份（1～12），输出这个月在哪儿个季度。
# 如果输入的是其他数，则提示您输错了 
'''
month = int(input("请输入1～12月之间的整数："))
if month == 1 or month == 2 or month ==3:
    print("%d月份所在一季度"%month)
elif month == 4 or month == 5 or month ==6:
    print("%d月份所在二季度"%month)
elif month == 7 or month == 8 or month ==9:
    print("%d月份所在三季度"%month)
elif month == 10 or month == 11 or month ==12:
    print("%d月份所在四季度"%month)
else :
    print("你输入的月份有误，请输入1～12的整数")
'''
'''
# 或者
month = int(input("请输入1～12月之间的整数："))
if month in (1,2,3):# 元祖
    print("%d月份所在一季度"%month)
elif month in [4,5,6]:# 列表
    print("%d月份所在二季度"%month)
elif 7 <= month <= 9 :# 区间
    print("%d月份所在三季度"%month)
elif month == 10 or month == 11 or month ==12:
    print("%d月份所在四季度"%month)
else :
    print("你输入的月份有误，请输入1～12的整数")
'''
month = int(input("请输入1～12月之间的整数："))
if 1 <= month <= 12 :
    if month < 3:
        print("%d月份所在一季度"%month)
    elif month in [4,5,6]:
        print("%d月份所在二季度"%month)
    elif 7 <= month <= 9 :
        print("%d月份所在三季度"%month)
    else: 
        print("%d月份所在四季度"%month)
else :
    print("你输入的月份有误，请输入1～12的整数")

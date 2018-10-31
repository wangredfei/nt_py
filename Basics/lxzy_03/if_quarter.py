# 练习
# 4输入一个季度是1～4输出这个季度有哪几个月份。
# 如果输入的不是1～4的整数，提示用户您错哪里了


quarter = int(input("请输入您想知道拿个季度的月份（1～4）:"))
if quarter == 1:
    print(quarter,"季度有1,2,3个月份")
elif quarter == 2:
    print(quarter,"季度有4,5,6个月份")
elif quarter == 3:
    print(quarter,"季度有7,8,9个月份")
elif quarter == 4:
    print(quarter,"季度有10,11,12个月份")
else :
    print("您输入的数字有误，请从新输入")


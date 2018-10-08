# 5
# 此示例示意条件表达式的语法和用法
# 商场促销 满100-20


money = int(input("请输入商品总额： "))

# 计算需要支付金额
pay = money - 20 if money >=100 else money
# 首先执行 if 语句 
# 可以理解为
'''
if money >=100:
    pay = money-20
else: 
    pay = money
'''
print("您需要支付： "，pay,"元")
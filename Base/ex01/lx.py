# a = 10000
# for i in range(10):
#     a = a *1.2
# print(a)
# -----------------------------------


# salary = 10000*1.2**10
# print('十几年后，您的薪资为:',salary)
# -----------------------------------

# name = "小赵"
# age = 22
# print("名字：",name,"年龄：",age)\

# -----------------------------------

# name = '金毛狮王'
# age = 66
# print("%s今年岁%d岁" % (name,age))
# -----------------------------------

'''
练习　：超市的西瓜７元一个．你有１００元，能买几个西瓜，找零多少

a = 100 % 7
b = 100 // 7
print("能买",b,"个西瓜，找零",a,"元")
'''
# -----------------------------------

'''
定义２个变量　，computer you ,值分别为：石头　布
终端输出：　电脑出拳　：石头　你出拳：　布　恭喜你赢了　


computer = "石头"
you = "布"

print("电脑出拳:%s你出拳:%s 恭喜你赢了!"%(computer,you))
'''
# -----------------------------------
'''
name = input("您叫什么名字：")
company = input("公司名称：")
salary = float(input("薪资："))

print ("我叫%s,我入职%s公司，薪资为%.2f元"%(name,company,salary)) 
'''
# -----------------------------------
# 3.

# r = 3
# L = 2*r*3.14
# S = 3.14*r**2
# print('周长为%d厘米,面积为%d平方厘米'%(L,S))

# -----------------------------------
# 4.
# g = 100//9
# m = 100%9
# print('能卖%d斤苹果，还剩%d元'%(g,m))
# -----------------------------------
# 5.
# w = 23*365//7
# int(w)
# print('过%d个星期天'%w) 

# -----------------------------------
#6 .
# h = 66666//3600
# m = 66666%3600//60
# s = 66666%60
# print('现在是%d时%d分%d秒'%(h,m,s))
# -----------------------------------


# 下面是01作业******************

# 空心三角形

for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    

    for k in range(i+1):
        if i == 0 or i ==4 or k == 0 or k==i:
            print("* ",end="")
        else: 
            print("  ",end="")
    print()
print()


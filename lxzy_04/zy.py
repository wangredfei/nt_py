# 练习:
#   1. 输入三行文字，让这三行文字在一个方框 内居中显示
#   如输入:
#      hello!
#      I'm studing python!
#      I like python!
#   显示如下:
#      +---------------------+
#      |        hello!       |
#      | I'm studing python! | 
#      |    I like python!   |
#      +---------------------+
'''
l1 = input("请输入第一行： ")
l2 = input("请输入第二行： ")
l3 = input("请输入第三行： ")
mll = max(len(l1),len(l2),len(l3))
print("+" + "-" * (mll + 4) + "+")
# 打印第一行
print("|"+l1.center(mll+4)+"|")
# 打印第二行
print("|"+l2.center(mll+4)+"|")
# 打印第三行
print("|"+l3.center(mll+4)+"|")
print("+" + "-" * (mll + 4) + "+")
'''



#   2. 用while循环打印 1 ~ 20 的整数(可以打印多行)  
''' 
i = 1
while i <= 20:
    print(i)
    i += 1
else: 
    pass
'''



#   3. 用while循环打印 1 ~ 20 的整数，打印在一行显示
#     每个数字之间用一个空格分隔
#      1 2 3 4 5 6 .... 18 19 20
'''
i = 1
while i <= 20:
    print(i,end=" ")
    i += 1
print()
'''

#   4. 用while循环打印 1 ~ 20的整数，每行打印5个，
#      打印4行,如:
#      1 2 3 4 5
#      6 7 8 9 10
'''
i = 1

while i <= 20:
    if i % 5 == 0 :
        print("%2d" % i)
    else:
        print("%2d" % i,end=" ")
    i += 1
print()
'''
#      ...
#   5. 输入一个整数n,打印一个宽度和高度都为n个字符的长方形
#     如:
#       请输入: 4
#     打印:
#       ####
#       #  #
#       #  #
#       ####
#     如:
#       请输入: 6
#     打印:
#       ######
#       #    #
#       #    #
#       #    #
#       #    #
#       ######
'''
# 纯函数（麻烦）
n = input("请输入一个整数： ")
# 判断输出的是否为整数
if n.isdigit():
    n = int(n)
    i = 1
    while i <= n:
        if i == 1 or i == n:
            j = 1
            while j <= n:
                print("#",end="")
                j += 1
            print()       
        else:
            k = 1
            while k <= n:
                if k == 1 or k == n:
                    print("#",end="")
                else:
                    print(" ",end="")
                k += 1
            print()
        i += 1  
else :
    print("您输入的有误，请输入一个整数")
'''

'''
# 用打印加函数的方法
n = input("请输入一个整数： ")
if n.isdigit():
    i = 1 
    n = int(n)
    print("#" * n )
    while i <= n-2 :
        print("#"+" "*(n-2)+"#")
        i += 1
    print("#" * n )
else :
    print("输入有误")  
'''  
'''
# 用 for 写

n = int(input("请输入一个整数： "))

for i in range(n): 
    for j in range(n):
        if i == 0 or i == n-1  or j == 0 or j ==n-1:
            print("#",end = "")
        else : 
            print(" ",end = "")
    print()
print()
'''
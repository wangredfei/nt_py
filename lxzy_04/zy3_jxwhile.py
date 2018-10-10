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
# 纯函数
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
# 用打印加函数的方法
n = input("请输入一个整数： ")
if n.isdigit():
    i = 2 
    n = int(n)
    print("#" * n )
    while i < n :
        print("#"+" "*(n-2)+"#")
        i += 1
    if n > 1:
        print("#" * n )

else :
    print("输入有误")  
 
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
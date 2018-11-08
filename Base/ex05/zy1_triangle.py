# 输入一个整数n，此整数代表三角形的直角边长
# 根据整数打印如下四中三角形
# 输入  3
# *
# **
# ***

#   *
#  **
# ***

# ***
# **
# *

# ***
#  **
#   *

# for 循环
'''
n = input("请输入整数： ")
if n.isdigit():
    n = int(n)
    # *
    # **
    # ***
    for i in range(1,n+1):
        print("*" * i)
    print("-" * 50)
    #   *
    #  **
    # ***
    for i in range(1,n+1):
        j = n-i
        print(" " * j + "*" * i)
    print("-" * 50)
    # ***
    # **
    # *
    for k in range(1,n+1):
        print("*" * (n + 1 - k))
    print("-" * 50)
    # ***
    #  **
    #   *
    for p in range(1,n+1):
        print(" " * (p - 1)+"*" * (n + 1 - p))
else:
    print("输入有误")
'''
# while循环
n = input("请输入整数： ")
if n.isdigit():
    n = int(n)
    # *
    # **
    # ***
    n1 = 1 
    while n1 <= n:
        print("*" * n1)
        n1 += 1 
    print("-"*50)
    #   *
    #  **
    # ***
    n2 = 1 
    while n2 <= n:
        print(" "*(n-n2)+"*" * n2)
        n2 += 1 
    print("-"*50)
    
    # ***
    # **
    # *
    n3 = 1 
    while n3 <= n:
        print("*" * (n+1-n3))
        n3 += 1 
    print("-"*50)

    # ***
    #  **
    #   *
    n4 = 1 
    while n4 <= n:
        print(" "*(n4-1)+"*" * (n+1-n4))
        n4 += 1 
else:
    print("输入有误")


# 熟悉循环嵌套
'''
for 循环写 

n = input("请输入一个整数： ")
if n.isdigit():
    n = int(n)
    # *
    # **
    # ***
    # i 控制行
    for i in range(1,n+1):
        # j控制列
        for j in range(1,i+1):
            print("*",end="")
        print()
    print()
    #   *
    #  **
    # ***
    # a 控制行
    for a in range(1,n+1):
        # 用k打印空格
        for b in range(n - a) :
            print(" ",end="")
        # 用j
        for c in range(1,a+1):
            print("*",end="")
        print()
    print()
    # ***
    # **
    # *
    # m 控制行
    for m in range(1,n+1):
        # j控制列
        for p in range(1 , n+2-m ):# 反着打印
            print("*",end="")
        print()
    print()
    # ***
    #  **
    #   *
    # 用x控制空格
    for x in range(1,n+1):
        # 用z打印空格
        for z in range(x-1) :
            print(" ",end="")
        # 用y控制每行打印的星星点数
        for y in range(1,n+2-x):
            print("*",end="")
        print()
    print()
else:
    print("输入有误")

'''
'''
# while写
n = input("请输入一个整数： ")
if n.isdigit():
    n = int(n)
    # a1 控制行数
    # *
    # **
    # ***
    
    a1 = 1
    while a1 < n+1:
        # b1 控制每行输入多少个*号
        b1 = 1
        while b1 < a1 + 1:
            print("*",end="")
            b1 += 1
        print()
        a1 += 1
    print("-"*50)

    #   *
    #  **
    # ***

    a2 = 1
    while a2 < n+1:
        # 下面打印空格
        p = 1
        while p < n + 1 - a2:
            print(" ",end="")
            p += 1
        # b2 控制每行输入多少个*号
        b2 = 1
        while b2 < a2 + 1:
            print("*",end="")
            b2 += 1
        print()
        a2 += 1
    print("-"*50)
    
    # ***
    # **
    # *
    
    a3 = 1
    while a3 < n+1:    
        b3 = 1
        while b3 < n + 2 - a3:
            print("*",end="")
            b3 += 1
        print()
        a3 += 1
    print("-"*50)
    # ***
    #  **
    #   *
    a4 = 1
    while a4 < n+1:
        # 下面打印空格
        p4 = 1
        while p4 < a4 :
            print(" ",end="")
            p4 += 1
        # b2 控制每行输入多少个*号
        b4 = 1
        while b4 < n + 2 - a4:
            print("*",end="")
            b4 += 1
        print()
        a4 += 1
   



    print()
else:
    pass
'''




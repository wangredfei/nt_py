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
'''
n  = int(input("请输入一个整数"))
i = 1
while i <= n :
    print("*"*i)
    i += 1
print("-"*30)
j = 1
while j <= n:
    print("*"*(n+1-j))
    j +=1
print("-"*30)
k = 1 
while k <= n:
    print(" "*(n-k)+"*"*k)
    k += 1
print("-"*30)
l = 1
while l <= n:
    print(" "*(l-1)+"*"*(n+1-l))
    l += 1
'''
# 2. 写一个程序,任意输入一个整数,判断这个整数是否是素数(prime)素数(也叫质数), 只能被1和自身整除的正整数
'''
n = int(input("请输入一个整数: "))
for i in range(2,n-1):
    if n % i == 0:
        print(" 不是素数 ")
        break
else:
    print ("是素数")
'''
# 12345
# 23456
# 34567
# 45678
# 56789
n = int(input("请输入一个整数: "))
for i in range(1,n+1):
    for j in range(i,i+n):
        print(j,end="")
    print()
print( )
# 2. 写一个程序,任意输入一个整数,判断这个整数是否是素数(prime)素数(也叫质数), 只能被1和自身整除的正整数
#    - 如:   2 3 5 7 11 13 17 19
#    - 提示:
#        - 用排除法,当判断x是否为素数时,只要让x分别除以2, 3, 4, ... x-1 ,只要有一个能整除,则x不是.素数,否则x是素数
'''
n = input("请输入一个整数: ")
if n.isdigit():
    n = int(n)
    for i in range(2,n):
        if n % i == 0:
            print("不是素数 ")
            break
    else:
        print("是素数")
'''

n = input("请输入一个整数: ")
if n.isdigit():
    n = int(n)
    i = 2
    while i <= n-1:
        if n % i == 0:
            print("不是素数 ")
            break
        i += 1
    else:
        print("是素数")



        
        

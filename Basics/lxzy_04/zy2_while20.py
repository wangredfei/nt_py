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

i = 1
while i <= 20:
    print("%2d" % i, end=" ")
    # 每第五个后面打印一个换行
    if i % 5 == 0 :
        print()
    i += 1
print()

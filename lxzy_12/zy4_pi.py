#   4. 写程序求:
#      1/1 - 1/3 + 1/5 - 1/7 + 1/9 .. (+-)1/(2*n-1)
#      的和
#      　n最大数取 1000000
#     打印这个和
#     打印这个和乘以4的值(圆周率)   
def mysumw(n):
    s_num = 0
    i = 1
    while i <= n:
        k = (-1)**(i-1)/(2*i-1)
        s_num += k
        i += 1
    return s_num
print(mysumw(1000000))
print(mysumw(1000000)*4)

'''
def mysum(n):
    # import sys
    # sys.setrecursionlimit(1000000)
    # print(sys.getrecursionlimit())
    s_num = 0
    if n == 1 :
        return 1
    k = (-1)**(n-1)/(2*n-1)
    s_num = k + mysum(n-1)
    return s_num
print(mysum(500))
'''
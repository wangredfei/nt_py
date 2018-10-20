# 集合是可变的容器,但是里面的元素必须是不可变的,元素是唯一的
# set() 创建空字典的唯一办法
# 1. 创建两个函数
# def sum3(a, b, c):
#     # 用于返回三个数的和
#     ....
# def pow3(x):
#     # 用于返回x的三次方
#     ...
# 用以上两个函数计算:
#     1. 计算1的立方 + 2的立方 + 3的立方 的和
#     2. 计算1+2+3的和的立方
#     即: 1**3 + 2**3 + 3 ** 3 和 (1+2+3)**3

def sum1(a, b, c):
    return a+b+c
def pow1(x):
    return x**3
print("1,2,3的立方和为: ",sum1(pow1(1), pow1(2), pow1(3)))
print("和的立方为: ",pow1(sum1(1, 2, 3)))
#   3. 编写函数,计算下列多项式的和:
#      Sn  = 1/(1*2) + 1/(2*3) + 1/(3*4) + ...
#          ... + 1/(n*(n+1))
#     def Sn(n):
#         ...
#     print(Sn(3))  # 0.75
#     print(Sn(1000))  # ???
def A(nub):
    sum_nub = 0
    for i in range(1,nub+1):
        sum_nub += 1/(i*(i+1))
    return sum_nub
print(A(3))
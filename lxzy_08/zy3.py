#   3. 编写函数,计算下列多项式的和:
#      Sn  = 1/(1*2) + 1/(2*3) + 1/(3*4) + ...
#          ... + 1/(n*(n+1))
#     def Sn(n):
#         ...
#     print(Sn(3))  # 0.75
#     print(Sn(1000))  # ???
def Sn(number):
    # 生成列表
    l = list(range(1,number+1))
    # 创建一个值用于存储总和
    sum_number = 0
    for i in l :
        sum_number += 1/(l[i-1]*(l[i-1]+1))
    return sum_number
print(Sn(3))
print(Sn(1000))

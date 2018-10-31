#   1. 完全数:
#     1 + 2 + 3 = 6  (6为完全数)
#     1, 2,3为都为6的因数(能被一个数x整除的数y,则y为
#          x的因数)
#     1 x 6 = 6
#     2 x 3 = 6
#     完全都是指除自身以外的所有因数之和相加等于自身的数
#     求4 - 5个完全数
#     答案:
#       6
#       28
#       496
#       ...

def get_ynub(n):
    l = []
    for i in range(1,n):
        if n % i == 0:
            l.append(i)
        continue
    return l

# n = int(input("请输入一个数:"))
# print(get_ynub(n))
def get_autonub(n):
    autonub_l = []
    i = 2
    while len(autonub_l) < n:
        l = get_ynub(i)
        if sum(l) == i and len(l)>2:
            autonub_l.append(i)
        i += 1
    for nub in autonub_l:
        print(nub)
n2 = int(input("您想要几个完全数: "))
get_autonub(n2)
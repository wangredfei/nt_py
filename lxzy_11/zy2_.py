#   2. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst) 打印出所有的数字
#        print_list(lst)  # 打印 3 5 8 10 13...
#     2) 写一个函数sum_list(lst) 返回这个列表中所有数字
#        的和
#        print(sum_list(L))  # 106
#     注:
#       type(x) 可以返回一个变量的类型
#          如:
#            >>> type(20) is int  # True
#            >>> type([1, 2, 3, 4]) is list  # True


# 1)
def print_list(l):
    for i in l:
        if type(i) is int:
            print(i)
        elif type(i) is list:
            print_list(i)

# 定义一个变量用于求和
s = 0
def sum_list(l):
    global s
    for i in l:
        if type(i) is int:
            # print(i)
            s += i
        elif type(i) is list:
            sum_list(i)
    return s


# 1)
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
print_list(L)
# 2)
print(sum_list(L))


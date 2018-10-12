
# 3. 有一些数字存于列表中,如:  L = [1, 3, 2, 1, 6, 4, 2, .....98, 82]
#     - 将列表中出现的数字存入到另一个列表l2中
#         - 要求 : 重复出现多次的数字只能在L2中保留一份(去重)
#     - 将列表中出现两次的数字存于L3列表中,在L3列表中只保留一份


l = [1,2,2,3,3,3,4,4,5,5,5,6,6,6,6,6,8,9]
# 定义三个空的列表
l1 = []
l2 = []
l3 = []
for i in l :
    count_nub = l.count(i)# 计算本次循环的数有几个
    if i not in l1: # 去重放入l1
        l1.append(i)
    elif count_nub == 2 : # 有两个的放入l2
        l2.append(i)
    elif count_nub > 2:# 打印有多个的元素分别是哪个
        if i  not in l3:# 去重要多用in \ not in
            print(i,"有",count_nub,"次")
        l3.append(i)
print(l1)
print(l2)
print(l3)
# 总结一下.想要去除重复,要想到 in  \ not in 
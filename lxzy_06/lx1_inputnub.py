# 用户每次输入一个数就存入列表，输入负数退出打印列表、平均值、最大值
# 第一种
'''
l = []
i = 0
sum_num = 0
while 1 :

    n = int(input("请输入一个数： "))
    if n > 0 :
        i += 1
        sum_num  += n 
        average = sum_num / i 
        l += [n]
    elif n < 0 :
        break
    else :
        print("请输入一个正整数")
print("l = ",l)
print("averger = ",average)
print("max = ",max(l))
'''
#第二种
'''
# 首先定义一个空列表
l = []
# 定义说如了几次
i = 0
# 定义输入的数字的和
sum_num = 0
while 1 :
    n = int(input("请输入一个数： "))
    # 判断是否时正整数
    if n > 0 :
        # 输入i次
        i += 1
        # 求和
        sum_num  += n 
        # 求平均数
        average = sum_num / i 
        # 放入列表
        l += [n]
        # 判断大小
        for k in l:
            # 如过大则拿入
            if k > n:
                max_num = k
            # 否则跳出本次循环
            else:
                continue
    # < 0 则结束循环
    elif n < 0 :
        break
    # 判断是否为0
    else :
        print("请输入一个正整数")
# 打印
print("l = ",l)
print("averger = ",average)
print("max = ",max(l))
'''
#第三种：
try:
    l = []
    while 1 :
        n = input("请输入一个数： ")
        if n.isnumeric():
            n = int(n)
            if n > 0 :
                l.append(n)
            else :
                print("请输入一个正整数")
        else: 
            break
    print("l = ",l)
    print("averger = ",sum(l)/len(l))
    print("max = ",max(l))
except ZeroDivisionError as p:
    print("列表为空")
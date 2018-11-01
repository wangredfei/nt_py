# 5. 写一个myrange函数,参数可以传1~3个,实际含义
#     与range函数规则相同,此函数返回符合range函数规则
#     的列表
#     如:
#       L = myrange(4)
#       print(L)  # [0, 1, 2, 3]
#       L = myrange(4, 6)
#       print(L)  # [4, 5]
#       L = myrange(1, 10, 3)
#       print(L)  # [1, 4, 7]
def myrange(*args):
    # 创建一个空的列表
    l = []
    # 判断长度
    if len(args) == 1:
        i = 0
        while i < args[0]:
            l.append(i)
            i += 1
    if len(args) == 2:
        i = args[0]
        while i < args[1]:
            l.append(i)
            i += 1
    if len(args) == 3:
        # 判断步数正反
        if args[2] > 0 :
            i = args[0]
            while i < args[1]  :
                l.append(i)
                i += args[2]
        elif args[2] < 0 :
            i = args[0]
            while i > args[1]:
                l.append(i)
                i += args[2]
    return l
print(myrange(5))
print(myrange(5,10))
print(myrange(5,15))
print(myrange(15,2,-3))
        

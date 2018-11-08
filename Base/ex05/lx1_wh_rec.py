# 12345
# 12345
# 12345
# 12345
# 12345
# 1. 先用循环控制打印的行数
# 2. 用另一个循环控制每行输出的结果
# *  要换行， 不要忘了改变循环变量
n = input("输入一个整数: ")
if n.isdigit():
    # 占位
    st = "%"+str(len(n)+2)+"d"
    n = int(n)
    # 控制行
    i = 1
    # 控制行数
    while i <= n :
        # 控制列
        j = 1 
        # 控制列数
        while j <= n:
            print(st % j,end="")
            j += 1
        print()
        i += 1
    print()
else :
    pass
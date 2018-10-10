# 输如n求
# 1 + ...+ n 的和
n = input("输入一个整数")
if n.isdigit():
    n = int( n )
    s = 0 # 累计计数
    i = 1 
    while i <= n:
        s += i # 累加
        i += 1 # 改变循环变量
    print(s)
else:
    print("错")

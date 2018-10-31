# 12345
# 23456
# 34567
# 45678
# 56789

n = input("输入一个整数")
if n.isdigit():
    
    i = 0 # 控制行
    st = "%"+str(len(n)+2)+"d" 
    n = int( n )
    while i < n:
        j = 1 + i # 让每行开头加1
        while j <= n + i:# 打印n次
            print( st % j,end="") 
            j += 1
        print()
        i += 1
else:
    print("输入有误，从新输入")

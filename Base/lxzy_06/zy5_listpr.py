# 5. 把 0 ~ 100 之 间的所有素数存于一个列表中  
#     即: L = [2, 3, 5, 7, 11, ..... 97]
l = []
for i in range(101):
    if i < 2: # 不是素数
        continue　　#继续
    for x in range(2,i):# 依次除以2~i-1, 当是2的时候for终止循环跳刀else
        if i % x == 0 :# 一定不是素数
            break# 跳出
    else:# 一定是素数 加进去
        l.append(i)
print(l)
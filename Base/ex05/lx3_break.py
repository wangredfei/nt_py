# 第一次输入：1
# 第一次输入：2
# 第一次输入：3
# 第一次输入：4
# 第一次输入：-1
# out ：10

s = 0
while 1:
    n = int(input("请输入"))
    if n < 0 :
        break
    s += n
print(s)
    
    
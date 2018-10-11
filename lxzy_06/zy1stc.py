
# 打印空心等边三角形

n = int(input("请输入整数"))

for i in range(1,n+1):
    
    if i == 1 or i == n:
        print(" " *(n-i)+"* "*i)
    else:
        print(" "*(n-i) + "*" + " "*(2*i-3) + "*")
    

'''

# 用for嵌套写
n = int(input("请输入整数"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        if i == 1 or i == n or k == 1 or k == i:
            print("* ",end="")
        else :
            print("  ",end="")
    print()
print()
'''
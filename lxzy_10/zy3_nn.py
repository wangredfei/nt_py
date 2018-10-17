
#   3. 给出一个数n,写一个函数计算:
#     1 + 2**2 + 3**3 + .... + n**n的和
def nn(n):
    a = 0
    for i in range(1,n+1):
        a += i**i 
    return a
print(nn(5))
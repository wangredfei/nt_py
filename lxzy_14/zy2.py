# 2. 分解质因数.输入一个正整数,分解质因数
#     如 输入: 90 则打印: 90=2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包括1))

def get_pr(n):
    '''用循环来实现质因数'''
    l = []
    while n != 1:
        for i in range(2,int(n)+1):
            if n % i ==0:
                l.append(i)
                n /= i
                break
    return l 
def print_formula(n):
    l = get_pr( n)
    s = "*".join([str(x) for x in l])
    print("{}={}".format(n,s))
n = int(input("输入一个数"))
print_formula(n)


# 2. 分解质因数.输入一个正整数,分解质因数
#     如 输入: 90 则打印: 90=2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包括1))
l = []
n = n1 = int(input("输入一个数"))
while n != 1:
    for i in range(2,int(n)+1):
        if n % i ==0:
            l.append(i)
            n /= i
            break
s = "*".join([str(x) for x in l])
print("{}={}".format(n1,s))
# 多思考
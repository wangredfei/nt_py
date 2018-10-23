# 2. 分解质因数.输入一个正整数,分解质因数
#     如 输入: 90 则打印: 90=2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包括1))


def pr():
    n = int(input("请输入一个大于2的数"))
    #定义一个不变的数
    b = n
    # 定义一个空的列表用于存入小于n的素数
    l = []
    # 第一存放结果元素的列表
    ll = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0: 
                break
        else :
            l.append(i)
    # print(l)
    for k in l:
        while  n/k == int(n/k):
            n /= k
            ll.append(k)
            if n == 1:
                break
    if ll[0]== b:
        print("这是素数")
    else:
        s = "*".join([str(x) for x in ll])
        print("{}={}".format(b,s))
try :        
    pr()
except:
    print("输入错误")
    
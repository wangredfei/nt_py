# 4. 写一个函数primes(n)  返回指定范围内的全部素数
#     (不包含n)的列表,打印印这些素数的列表, 如:
#       def primes(n):
#           ...
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#     1) 打印 100以内的素数
#     2) 打印 200以内全部素数的和

def primes(n):
    count_l = []
    for i in range(2,n):
        # 除以2到本身的前一个数
        for j in range(2,i):
            if i % j ==0:
                break
        else:
            count_l.append(i)
    return count_l
print(primes(100))
print(sum(primes(200)))
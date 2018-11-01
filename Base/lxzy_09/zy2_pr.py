
#  2. 写一个函数isprime(x) 判断x是否为素数.如果为素数
#     返回True,否则返回False
#     如:
#       print(isprime(3))  # True
#       print(isprime(4))  # False

    
def isprime(s):
    if  s < 2:
        return False
    for i in range(2,s):
        if s % i == 0 :
            return False
    return True
print(isprime(3))
print(isprime(9))

 
#  3. 写一个函数prime_m2n(m, n) 返回从m开始,到n结束
#     范围内的全部素数的列表,并打印对应的列表 (不包含n)
#     如:
#       def prime_m2n(m, n):
#            ...
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]



def prime_m2n(m, n):
    # count_l =[]
    # for s in range(m,n):
    #     if isprime(x):
    #         count_l.append(s)
    # return count_l
    return [x for x in range(m,n) if isprime(x)]
L = prime_m2n(10, 20)
print(L)

# 4. 写一个函数primes(n)  返回指定范围内的全部素数
#     (不包含n)的列表,打印印这些素数的列表, 如:
#       def primes(n):
#           ...
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#     1) 打印 100以内的素数
#     2) 打印 200以内全部素数的和

def primes(n):
    # return  [x for x in range(100) if isprime(x)]
    return prime_m2n(0,n)
print(primes(100))
print(sum(primes(200)))
        
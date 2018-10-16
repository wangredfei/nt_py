
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

 

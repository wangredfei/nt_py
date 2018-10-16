#  3. 写一个函数prime_m2n(m, n) 返回从m开始,到n结束
#     范围内的全部素数的列表,并打印对应的列表 (不包含n)
#     如:
#       def prime_m2n(m, n):
#            ...
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]



def prime_m2n(m, n):
    count_l =[]
    for s in range(m,n):
        if  s < 2:
            continue
        for i in range(2,s):
            if s % i == 0 :
                break
        else :
            count_l.append(s)

    return count_l
L = prime_m2n(10, 20)
print(L)
    
        

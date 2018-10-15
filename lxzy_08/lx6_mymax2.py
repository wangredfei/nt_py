def mymax2(a, b, c):
    max_num = a 
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num
print(mymax2(100, 200, 300))
print(mymax2("ABC", 'abc', '123')) 
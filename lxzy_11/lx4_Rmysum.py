def mysum(n):
    if n == 1:
        return 1
    s =  n+mysum(n-1)
    return s
print(mysum(100))
print(mysum(10000))
# 用while循环
'''
def myeven(start,stop):
    
    while start < stop:
        if start  % 2 ==0 :
            yield start
        start += 1
evens = list(myeven(10,20))
print(evens)
for x in myeven(21,30):
    print(x)
'''
# 用for循环
def myevenf(start,stop):
    for i in range(start,stop):
        if start % 2 == 0:
            yield i
        start += 1
        
print(list(myevenf(50,60)))
def myfilter(fn,iterable):
    for i in iterable:
        if fn(i) != 0:
            yield i
       
for i in myfilter(lambda x : x % 3  ,range(10)):
    print(i)
for i in filter(lambda x : x% 3,range(10)):
    print(i)
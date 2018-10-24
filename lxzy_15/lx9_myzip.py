def myzip(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    while 1 :
        try :
            x = next(it1)
            y = next(it2)
            yield (x,y)
        except  StopAsyncIteration:
            return
A = [1,2,3,4,5,6,7]
B = ['a','b','c','d', 'e','f','g']
for i in myzip(A,B):
    print(i)

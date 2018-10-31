l = [2,3,4,5,6]
# for i in l:
#     print(i)
k = iter(l)
while 1:
    try:
        print(next(k))
    except StopIteration.:
        break 
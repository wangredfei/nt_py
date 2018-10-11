# l = [x for x in range(101) if x % i != 0  for i in range(2,x-1) ]
l = []
for i in range(101):
    if i == 0 or i == 1:
        continue
    elif i == 2 : 
        l.append(i)
    else:
        for x in range(2,i):
            if i % x == 0 :
                break
        else:
            l.append(i)
print(l)
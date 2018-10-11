# 5. 把 0 ~ 100 之 间的所有素数存于一个列表中  
#     即: L = [2, 3, 5, 7, 11, ..... 97]
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
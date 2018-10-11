
l = [1,2,2,3,3,3,4,4,5,5,5,6,6,6,6,6,8,9,8,56,9,5,0,1,5,7,5,9,4,6,54,486,4,6,96,7,8,9,7,8,7,8,7,11,22,33,11]
l1 = []
l2 = []
l3 = []
for i in l :
    
    count_nub = l.count(i)
    
    if i not in l1:
        l1.append(i)
    elif count_nub == 2 :
        l2.append(i)
    elif count_nub > 2:
        if i  not in l3:
            print(i,"有",count_nub,"次")
        l3.append(i)
    
        

print(l1)
print(l2)

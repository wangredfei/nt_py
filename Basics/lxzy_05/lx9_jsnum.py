# 求1～100 之间所有不能被2,3,5,7 整除的数的和



c = 0
for i in range(1,100):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 :
        continue
    c += i
print(c)
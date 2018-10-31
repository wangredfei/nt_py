lis = []
while 1:
    n = input("输入一个整数")
    
    n = int(n)
    if n<0 :
        break
    elif n == 0 :
        print("请输入正整数")
    lis.append(n)
print("最大的数是:",max(lis))
lis2 = lis.copy()
zuida = max(lis2)
while zuida in lis2:
    lis2.remove(zuida)
sec_num = max(lis2)
# print(lis2)
# max_num = max(lis2)
# lis2.remove(max_num)
# max_num2= max(lis2)
# sec_index_num = lis2.index(max_num2)
# sec_num = lis2.pop(sec_index_num)
print("第二大的数是",sec_num)
min_nub = min(lis)
while min_nub in lis:
    lis.remove(min_nub)

print("删除过后列表为:",lis)
# 练习1 
'''
a = 100
b = 200
s = input("请输入a+b")
m = eval(s)
n = exec(s)
print(m)# 300 ,原因是eval是把字符串当成表达式来执行,返回执行结果
print(n)# None ,原因是exec 是把字符串当做程序来执行,返回None
'''
# 练习2
# 1)
'''
# l1 = [6, 8, 11]
l1 = [x for x in map(lambda x , y :x+y , [1,2,3,4],[5,6,8])]
print(l1)
# 2)
for i in filter(lambda x :True if x%2==0 else False , l1 ):
    print(i)
'''
# 练习3
D = [{"name":"Green","age":30},{"name":"bob","age":25}]
A = sorted(D , key = lambda d : d["age"])
print(A)
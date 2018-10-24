s = {'tangse','sundasheng','zhubajie','baigujing','shawujin'}
for i in s:
    print(i)
else :
    print("jieshu")
# people = iter(s)
# 注意
# while 1 :
#     try:
#         print(next(iter(s)))
#     except StopIteration:
#         print("遍历结束")
#         break


迭代器
it  = iter("123123")
print(it)
print(next(it))
print(next(it))
print("-"*50)
for i in it :
    print(i)
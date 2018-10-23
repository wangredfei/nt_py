s = {'tangse','sundasheng','zhubajie','baigujing','shawujin'}
# for i in s:
#     print(i)
# else :
#     print("jieshu")
# people = iter(s)
while 1 :
    try:
        print(next(iter(s)))
    except StopIteration:
        print("遍历结束")
        break

# 以有列表,值是键的长度,存在字典
L = ['terena','xiaozhang','xiaowang']
book = {x : len(x) for x in L }
# for i in L :
#     book[i] = len(i)
print(book)
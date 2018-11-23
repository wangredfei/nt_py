import re

s = "Hi,This is Jame"
it = re.finditer(r'[A-Z]\w+', s)
# print(next(it))
# print(next(it))
# print(next(it))

# for i in it:
#     print(i.group())# 获取match对象对应字串
try:
    obj = re.fullmatch(r'\w+','port123')
    print(obj.group())
except AttributeError as e:
    print(e)

obj = re.search(r'\d+','138-1371-1589')
print(obj.group()
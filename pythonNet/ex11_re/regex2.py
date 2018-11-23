import re
pattern = r'(ab)cd(?P<dog>ef)'
regex = re.compile(pattern)
obj = regex.search("abcdefghi",0,6)
print(obj.group())
# 属性
# pos
# endpos
print(obj.pos)# 目标字串开始位置
print(obj.endpos)# 目标字串结束位置
print(obj.re) # 正则表达式
print(obj.string) # 目标字符串
print(obj.lastgroup)# 显示最后一组组名,如果没有名字则显示不出来
print(obj.lastindex)# 最后一组序列号
print(obj.start())# 匹配内容的开始位置
print(obj.end())# 匹配内容的结束位置
print(obj.span())# 匹配内容的起止位置
print(obj.group())# 获取match对象的对应内容,
print(obj.group(2))# 获取match对象的对应内容,
print(obj.group('dog'))# 获取match对象的对应内容,
print(obj.groupdict())# 获取捕获组和对应值的字典
print(obj.groups())# - 获取所有子组对应内容

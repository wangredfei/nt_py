# - 写程序数入一个字符串，打印字符串中的如下内容
#         1. 打印这个字符串的第一个字符
#         2. 打印这给字符串最后一个字符
#         3. 如果这个字符串的长度是奇数，打印中间这个字符


s = input("输入字符串：")
print(s[0])
print(s[-1])
# 中间字符索引位置
a = len(s) // 2
if len(s) % 2 == 1 :
    print(s[a])
else :
    pass
    
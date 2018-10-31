'''
s = input("请输入一个字符串")
# 计算中文数
chi = 0
# 计空格数
space_num = 0
# print("空格的个数是",s.count(" "))
for i in s :
    if ord(i) > 128 :
        chi += 1
    elif i == " ":
        space_num += 1
print("您输入有%d个空格，%d 个汉字" % (space_num,chi))
'''
# 用 while 写
s = input("请输入一个字符串")
i = 0
chi = 0
space_num = 0

while i < len(s):
    n = s[i] 
    if ord(n) > 128 :
       chi += 1 
    elif n == " ":
        space_num += 1
    i += 1
print("您输入有%d个空格，%d 个汉字" % (space_num,chi))


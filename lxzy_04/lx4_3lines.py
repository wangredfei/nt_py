# - 练习：
#     - 输入三行文字，让这三行文字一次以20个字符的宽度右对齐显示
#     - 如：
#         - 输入第一行： hello world
#         - 输入第二行： abcd
#         - 输入第三行： aaaaaaa
#     - out：
#                 hello world
#                        abcd
#                     aaaaaaa
#     -
l1 = input("输入第一行： ")
l2 = input("输入第二行： ")
l3 = input("输入第三行： ")
# print("%20s\n%20s\n%20s"%(l1,l2,l3))

# 能否以最长的字符串的长度进行右对齐显示（左侧空格）
ll = len(max(l1,l2,l3))
print(type(ll))
# print(ll)

# print(' ' * (ll - len(l1))+l1)
# print(' ' * (ll - len(l2))+l2)
# print(' ' * (ll - len(l3))+l3)
# print("--------------")
# ss = "%" + str(ll)+"s"
# print(ss%l1)
# print(ss%l2)
# print(ss%l3)


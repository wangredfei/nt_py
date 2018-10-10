# 练习:
#   1. 输入三行文字，让这三行文字在一个方框 内居中显示
#   如输入:
#      hello!
#      I'm studing python!
#      I like python!
#   显示如下:
#      +---------------------+
#      |        hello!       |
#      | I'm studing python! | 
#      |    I like python!   |
#      +---------------------+

l1 = input("请输入第一行： ")
l2 = input("请输入第二行： ")
l3 = input("请输入第三行： ")
mll = max(len(l1),len(l2),len(l3))
print("+" + "-" * (mll + 4) + "+")
# 打印第一行
print("|"+l1.center(mll+4)+"|")
# 打印第二行
print("|"+l2.center(mll+4)+"|")
# 打印第三行
print("|"+l3.center(mll+4)+"|")
print("+" + "-" * (mll + 4) + "+")






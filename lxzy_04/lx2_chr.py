# 1. 写一个程序，输入一段字符串，如果字符串不为空，则把一个字符的编码值打印出来
# x = input("请输入： ")
# if x :
#     xx = x[0]
#     xxo = ord(xx)
#     print("%s的编码值是%s"%(xx,xxo))
# else :
#     print("输入有误")

# 2. 写一个程序，输入一个整数（0～65535），打印这个数值对应的字符

c = input("输入一个整数(0~65535)： ")

if c.isdigit():
    c = int(c)
    if 0 < c < 65535 :
        print(chr(c))
    else :
        print("输入有误，请输入（0～65535）之间的整数")
else:
    print("输入有误,请重新输入")

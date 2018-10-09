# 输入一个字符串
# 1 判断您输入的字符有几个空格
# 2 去掉空格输出
# 3 输入数字 判断是否大于100

s = input("请输入一个字符串： ")
n = s.count(" ")
print("您输入有%d个空格" % n)  
rmk = s.rstrip()
print("去掉空格后",rmk)
if s.isdigit() :
    s = int (s)
    if s > 100 :
        print(">100")
    elif s < 100 : 
        print("<100")
    else:
        print("=")
    # print(bool(s>100))
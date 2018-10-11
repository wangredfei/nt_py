# 用户输入三次
# 当输入seven 密码： 123 时成功
# 否则失败，三次后禁止输入

'''
i = 1
while i <= 3:
    name = input("请输入用户名称：")
    password = input("请输入密码")
    if name == 'seven' and password == "123":
        print("登陆成功")
        break
    else :
        print("登录失败%d次,请从新输入" % i)
        i += 1      
else :
    print("您输入错误三次，禁止输入")

'''

for i in range(1,4):
    name = input("请输入用户名称：")
    password = input("请输入密码")
    if name == 'seven' and password == "123":
        print("登陆成功")
        break
    else :
        print("登录失败%d次,请从新输入" % i)
else :
    print("您输入错误三次，禁止输入")

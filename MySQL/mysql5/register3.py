from mysqlp import Mysqlp
from hashlib import sha1
print("(1) 注册")
print("(2) 登录")
print("(q) 退出")
while 1:
    menu = input("输入操作序号")
    if menu == "1":
        #1. 让用户输入用户名
        uname = input("请输入注册名: ")
        #2. 到数据库user表中去查
        sqlh = Mysqlp("db5")
        r = sqlh.all("select username from user where username=%s",[uname])
        if  r:
            print("该用户名已存在")
        else :
            pwd1 = input("请输入密码:")
            pwd2 = input("请再次输入密码:")
            if pwd1==pwd2:
                
                # 对密码加密存入数据库
                s = sha1()
                # 创建sha1加密对象
                s.update(pwd1.encode("utf8")) 
                # 转成字节流
                pwd = s.hexdigest() # 返回十六进制加密结果
                sqlh.zhixing('insert into user values (%s,%s)',[uname,pwd])
                print("恭喜注册成功")
            else:
                print('两次密码不一致,请重新输入')
    elif menu == '2':
        sqlh = Mysqlp('db5')

        uname = input("请输入用户名")
        pwd = input("请输入密码:")
        s = sha1()
        s.update(pwd.encode('utf8'))
        pwd2 = s.hexdigest()
        sql = 'select password from user where username=%s'

        result = sqlh.all(sql,[uname])
        if len(result) == 0:
            print("用户名错误")
        elif result[0][0] == pwd2:
            print("登陆成功")
        else:
            print("密码错误")
    elif menu == "q":
        print("已经退出")
        break
    else:
        print("输入错误,请重新输入")
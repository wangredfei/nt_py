from mysqlp import Mysqlp
from hashlib import sha1
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
        print('傻逼,这都输不对')
#3. 判断
from mysqlp import Mysqlp
from hashlib import sha1

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
    
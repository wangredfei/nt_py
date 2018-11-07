from mysqlp import Mysqlp

# 创建对象

sqlh = Mysqlp("db5")
 
sqlh.zhixing('update t1 set score = 100 where name = "安付伟"')

r = sqlh.one("select * from t1")
rr = sqlh.many("select * from t1",2)
rrr = sqlh.all("select * from t1")
print(r)
print(rr)
print(rrr)
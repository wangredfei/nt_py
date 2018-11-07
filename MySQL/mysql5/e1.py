'''在db5.t1表中插入一条记录'''
import pymysql

# 创建数据库链接对象
db = pymysql.connect("localhost","root","tarena","db5",charset="utf8")
# 利用数据库链接对象 来创建一个游标对象
cursor = db.cursor()
# 执行你的sql命令 
cursor.execute("insert into t1(name,score) values('安付伟',99);")
# 提交到数据库执行
db.commit()
# 关闭游标对象
cursor.close()
# 断开与数据库连接对象
db.close()
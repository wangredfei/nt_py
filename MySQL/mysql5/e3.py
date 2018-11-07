import pymysql

db = pymysql.connect(host='localhost', 
                    user='root', 
                    password='tarena', 
                    database='db5', 
                    charset='utf8')
cursor = db.cursor()
sel = 'select * from t1'
cursor.execute(sel)

# 结果为元组
one = cursor.fetchone()
print(one)
# 结果为大元组,每一条记录为小元组
many = cursor.fetchmany(2)
print(many)
# 结果为大元组,每一条记录为小元组
all = cursor.fetchall()
print(all)


db.commit()
cursor.close()
db.close()
'''此示例示意传参时,第二个元素要传入列表'''
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='tarena',
    charset='utf8', 
    database='db5'
)
cur = db.cursor()
iname = input("请输入学生姓名: ")
iscore = input("请输入学生成绩: ")
try:
    ins = 'insert into t1(name,score) values(%s,%s)'
    cur.execute(ins,[iname,iscore])
    db.commit()
    print("ok")
except:
    db.rollback()
cur.close()
db.close()



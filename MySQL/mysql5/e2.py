import pymysql

cnn = pymysql.connect(host='localhost', 
                        user='root', 
                        password='tarena', 
                        database='db5',
                        charset='utf8',
                        port=3306)

cur = cnn.cursor()
try:
    ins = 'insert into t1(name,score) values\
            ("小姐姐",100)'
    cur.execute(ins)

    upd = 'update t1 set score=100 where name="李白"'
    cur.execute(upd)

    dele = 'delete from t1 where name="杜甫"'
    cur.execute(dele)
    cnn.commit()

except:
    cnn.rollback()
    print("返回")
cur.close()
cnn.close()
import pymysql

class Mysqlp():
    def __init__(self,database,
                host='localhost',
                user='root',
                password='tarena',
                charset='utf8', 
                port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    def open(self):
        self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            charset=self.charset, 
            database=self.database,
            port=self.port
        )        
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,l=[]):
        self.open()
        self.cur.execute(sql, l)
        self.db.commit()
        self.close()
    
    def one(self, sql, l=[]):
        '''此方法指fetchone'''
        self.open()
        self.cur.execute(sql,l)
        result = self.cur.fetchone()
        self.close()
        return result
    def many(self, sql, n=1,l=[]):
        '''此方法指fetchmany'''
        self.open()
        self.cur.execute(sql,l)
        result = self.cur.fetchmany(n)
        self.close()
        return result
    def all(self, sql, l=[]):
        '''此方法指fetchall'''
        self.open()
        self.cur.execute(sql,l)
        result = self.cur.fetchall()
        self.close()
        return result

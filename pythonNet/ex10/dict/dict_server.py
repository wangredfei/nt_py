from socket import *
import pymysql
import os,sys
from threading import Thread

# 创建全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST, PORT)
DICT_TEXT = './dict.txt'

def do_child(c,db):
    '''接受判断'''
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        elif data[0] == "R":
            do_register(c, db, data)        
        elif data[0] == 'L':
            do_login(c, db, data)
        elif not data[0] or data[0] == 'Q':
            c.close()
            break
        elif data[0] == "S":
            do_select(c, db, data)

        elif data[0] == "C":
            do_hist(c, db, data)

def do_register(c, db, data):
    '''注册'''
    l = data.split(" ")
    name = l[1]
    password = l[2]
    cursor = db.cursor()
    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r:
        c.send(b'EXISTS')
        return
    sql1 = "insert into user(name,password) values('%s','%s');"%(name,password)
    try:
        cursor.execute(sql1)
        db.commit()
        c.send(b"OK")
    except:
        db.rollback()
        c.send(b"FALL")

def do_login(c, db, data):
    '''登录'''
    l = data.split(" ")
    name = l[1]
    password = l[2]
    cursor = db.cursor()
    sql = "select password from user where name = '%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if not r:
        c.send(b"FALL")
    elif r[0] == password:
        c.send(b"OK")
    else:
        c.send(b"NN")
    
def do_select(c, db, data):
    '''查询'''
    l = data.split(" ")
    name = l[1]
    word = l[2]
    cursor = db.cursor()
    sql = "select interpret from words where word = '%s'"% word
    cursor.execute(sql)
    r = cursor.fetchone()
    if not r :
        c.send(b"NO")
    else:
        c.send(r[0].encode())
        sql1 = "insert into hist(name,word,time) values('%s','%s',now());"%(name,word)
        try:
            cursor.execute(sql1)
            db.commit()
        except:
            db.rollback()

def do_hist(c, db, data):
    '''查记录'''
    l = data.split(" ")
    name = l[1]
    cursor = db.cursor()
    sql = "select word,time from hist where name = '%s'"% name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r :
        c.send(b"NO")
    else:
        s = ""
        for t in r:
            s += "\t".join(t)+"\n"
        c.send(s.encode())

def zomble():
    os.wait()

# 主函数
def main():

    # 创建数据库链接对象
    db = pymysql.connect('localhost','root','tarena','dict')

    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print("listen...")

    # 循环接受链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from ",addr)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常",e)
            continue


        f = os.fork()
        if f == 0:
            s.close()
            do_child(c,db)
            os._exit(0)#?
        else :
            c.close()
            t = Thread(target=zomble)
            t.setDaemon(True)
            t.start()
            continue

main()
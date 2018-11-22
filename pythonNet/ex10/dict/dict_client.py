from socket import * 
import sys
import getpass


HOST = sys.argv[1]
PORT = sys.argv[2]
ADDR = (HOST,int(PORT))


def menu():
    print("===================")
    print("=====  1.注册  =====")
    print("=====  2.登录  =====")
    print("=====  3.退出  =====")
    print("===================")

def menu2():
    print('''
        ============查询界面============
        --1.查词  2.历史记录  3.注销--
        ===============================
        ''')
def do_register(s):
    while True:
        name = input("输入您的姓名")
        password = getpass.getpass("输入密码")
        password1 = getpass.getpass("再次输入密码")
        if (" "in name) or (" "in password):
            print("用户名或密码不允许有空格")
        if password != password1:
            print("两次输入密码不一致")
            continue
        msg = "R %s %s"%(name,password)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data =="OK":
            print("注册成功")
        elif data == "EXISTS":
            print("该用户已存在")
        else: 
            print("注册失败")
        return

def do_login(s) :
    name = input("User:")
    password = getpass.getpass(">>>")
    msg = "L %s %s"%(name,password)
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == "OK":
        print("登录成功")
        login(s,name)
    elif data == "NN":
        print("登录失败,密码错误")
    else :
        print("没有注册")
    
def login(s,name):
    '''这个函数是二级页面客户端操作'''
    while True:
        menu2()
        try:
            num = int(input("请输入您想实现的功能"))
        except :
            print("命令错误")
            continue
        if num not in [1,2,3]:
            print("输入有误")
            continue
        elif num == 1:
            do_select(s,name)
        elif num == 2:
            do_hist(s,name)
        elif num == 3:
            break

def do_select(s,name):
    while True:
        word = input("请输入您想查的词, ##退出 : ")
        if word == "##":
            break
        msg = "S %s %s"%(name, word)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == "NO":
            print("没有这个词,请从新输入")
        else:
            print(data)

def do_hist(s,name):
    msg = "C %s"%name
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == "NO":
        print("没有记录")
    else:
        print(data)
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    try:

        s.connect(ADDR)
    except Exception as e:
        print("服务器异常",e)
        return
    while True:
        menu()
        try:
            num = int(input("请输入您想实现的功能"))
        except :
            print("命令错误")
            continue
        if num not in [1,2,3]:
            print("输入有误")
            continue
        elif num == 1:
            do_register(s)
        elif num == 2:
            do_login(s)
        elif num == 3:
            s.send(b'Q')
            s.close()
            sys.exit("谢谢使用")
      

        
main()
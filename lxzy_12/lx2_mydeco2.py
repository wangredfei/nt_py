# 此示例示意装饰器的用途和作用
# 模拟银行项目
#　业务：存钱和取钱
def per_check(fn):
    def fx(name,x):
        print("正在验证权限...通过")
        fn(name,x)
    return fx
def send_message(fn):
    def fy(n,x):
        fn(n,x)
        print("给{}发送信息".format(n))
    return fy
@ per_check
def save_money(name,x):
    print("{}存入{}元".format(name , x))
@ per_check
@ send_message
def withdraw(name, x):
    print("{}取出{}元".format(name , x))


# 另一个人写的程序
save_money("小王",200)
save_money("小赵",400)
withdraw("小钱",500)

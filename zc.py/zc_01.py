# 一:选择 C A B 
# 二 : 填空
# 1.  is :比较左右两者是不是同一个对象,可以理解成比较id ,真返回True ,否则False  
#     in : 判断左侧对象是否存在于右侧对象中 
#     =  : 右侧对象赋值给左侧
#     == : 比较 相等返回True,否则False
# 2. a = [1,9,25,49]
# 3. l2 = l[:3]
# 4. None
# 5. complex(3, 4)
# 6.[1,2,3,1,2,3,1,2,3]
# 7. False
# 8. [6,7,9,11]
# 三 编程题
# 1. 
'''
l = list(range(1,101))
print(l)
l1 = l[:10]
print(l1)
l2 = l[2::3]
print(l2)
l3 = l[4:51:5]
print(l3)
'''
# 2. 
'''
n = input("输入一个整数") 
if n.isdigit():
    n = int(n)
    for i in range(1,n+1):
        print("*" * i)
    for i in range(1,n+1):
        print("*" * (n-i))
    print()
else :
    print("输入有误")
'''

# 3.99
'''
# 控制行
for i in range(1, 10):
    # 控制列
    for j in range(1, i+1):
        # 占位
        zw = '%2d * %2d = %2d' % (j ,i ,i*j)
        print("%-15s" % zw ,end = "" )
    print()
'''

# 4 .

'''
s = "I am a girl!"
# 转成列表
l = s.split()
# 翻转
l2 = l[::-1]
# 转回字符串
s2 = " ".join(l2)
print(s2)
'''

# 思考题:

# 首先创建商品
goods = [
    {"name":"电脑","price": 1999},
    {"name":"鼠标","price": 10},
    {"name":"游艇","price": 20},
    {"name":"美女","price": 98},
        ] 
# 打印价目表
print("价目表".center(20))
print("-"*20)
# 定义序号
i = 1
# 创建列表让序号和键值关联
n_name = []
# 根据序号创建列表
l = []
# 创建字典
for good in goods:
    # 创建一个字典
    book = {}
    # 打印商品表
    print("%s. %s : %d元"% (i,good["name"],good["price"]))
    # 让价格和序号关联
    # 传入参数
    book[i] = good["price"]
    l.append(book)
    # 让价格和名字关联
    n_name_d = {}
    n_name_d[i] = good["name"]
    n_name.append( n_name_d ) 
    # 计数
    i += 1
print(l)
print(n_name)

# 输入总资产
m = int(input("请输入总资产: "))
# 开始买东西,定义一个购物车
gwc = []
# 定义一个参数,用于放入商品总额
g_pay = 0
while 1:
    pay = int(input("请输入您想选购的商品(输入-1退出): "))
    # 判断输入-1退出
    if pay == -1 :
        print("购买成功,您购买了%s,还剩余%d元" % (gwc , m - g_pay))
        break
    # 判断输入值与价格和名称的关系
    for q in l :
        # 打印键值
        for k,v in q.items():
            if pay == k:
                g_pay += v
    for p in n_name:
        for k2,v2 in p.items():
            if pay == k2:
                gwc.append(v2)
    
    # 判断购买所花金额是否超出 
    if g_pay > m :
        print("您的余额不足,购买失败") 
        print("您购买了%s,超出了%d元" % (gwc,g_pay-m))  
        break
    else :    
        print("购买成功,您购买了",gwc)
        
























# # AID1809班第一阶段周考题

# 一、选择题
# 1. 关于Linux系统下面说法错误的是（ C）
# 	A: Linux系统是至今最成功的开源操作系统内核之一
# 	B: Linux系统是多任务、多用户系统	
# 	C: Linux系统没有病毒
# 	D: Linux系统因为开源，所以安全性不好

# 2. 关于Linux命令以下说法正确的是？（ A）
# A: cd 命令可以切换工作目录
# B: touch命令只能创建空文件
# C: cp 命令只能在同一个目录下复制文件
# D: mv 命令只能在不同的目录间搬移文件

# 3. /home/tarena目录下有文件a.txt，现希望所有用户都具有读权限，属主用户具有写权限，以下命令正确的是？（ B）
# 	A: chmod  a+r-wx,u+w  /home/tarena/a.txt
# 	B: chmod  644  /home/tarena/a.txt
# 	C: chmod  –a+r-wx,-u+w  /home/tarena/a.txt
# 	D: chmod  755  /home/tarena/a.txt

# 二、填空题
# 1.is、in、=、==四者的含义和区别：_______________
# _____________________________________________

# 2.a = [i ** 2 for i in range(9) if i % 2 != 0]   a = ____________________

# 3.L = ['Adam', 'Lisa', 'Bart', 'Paul']，取前三个元素                     
# 4. 在Python中    表示空类型。
# 5.以3为实部4为虚部，Python复数的表达形式为       或      。
# 6.表达式[1,2,3]*3的执行结果为             .
# 7.表达式“[3] in [1,2,3,4]”的值为         。
# 8.假设列表对象aList的值为[3,4,5,6,7,9,11,13,15]那么切片aList[3:7]得到的值是 
#            。
# 三、编程题：
# 1.利用range创建列表[1,2,3,…,100]
# 	请利用切片取出：
# 	（1）前10个数；
# 	（2）3的倍数；
# 	（3）不大于50的5的倍数

# 2.当输入相应的数字时，请打印出如下图形
#    当输入3时，打印出：


# *
# **
# ***
# **
# *
# 	当输入5时：
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# 3.请打印出九九乘法表
# 4.将‘I am a gril’按照‘gril a am I’的格式输出
# 四、思考题
# 购物车功能要求：
# 要求用户输入总资产，例如： 2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# goods = [
# {"name":"电脑","price":1999},
# {"name":"鼠标","price":10},
# {"name":"游艇","price":20},
# {"name":"美女","price":98},
# ]
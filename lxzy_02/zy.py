# **************************作业
#1.
x = int(input("第一个整数："))
y = int(input("第二个整数："))
z = pow(x,y)
zz = x + y
print('和为'zz)
print("x的y次方为"z)
#2. 
h = int(input("小时： "))
m = int(input("分钟： "))
s = int(input(" 秒 ： "))
ss = h*3600 + m*60 + s
print("过了%d秒" % ss)

# 3.
salary = int(input("输入你的社保基数："))
# 个人缴费比例
ylg = salary*0.08
ybg = salary*0.02+3
zfg = salary*0.12
# 单位
yld = salary*0.19
gsd = salary*0.005
ybd = salary*0.10
zfd = salary*0.12

# 各项缴费明细
yl = ylg + yld
gs = gsd
yb = ybg + ybd
zf = zfg + zfd
# 个人总 缴费金额
grze =  ylg + ybg + zfg
# 单位缴费金额
gsze = yld + gsd + ybd + zfd
# 国家收到
gjze = grze + gsze
# 打印
print("养老：%d,工商：%d,医疗：%d,住房：%d"%(yl,gs,yb,zf))
print("个人总额%d" % grze)
print("单位总额%d" % gsze)
print("公司收到%d" % gjze)

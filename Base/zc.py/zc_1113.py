# # 一
# # 	B 一
# 	B B C  D  A  D    
# 二　
# 	１．ＡＢＣＤ
# 	２．ＡＢＣ
# 	３．ＡＢＣＤ
# 	４．ＡＣＤ
# 	５．ＡＤ
# 	６．ＢＤ
# 三　：
# １．name.insert(2,"T")　或者　切片赋值　name[2:2]="T"
# ２．单双引号三引号都可以作为字符串引用 可以穿插混合使用,三引号可以换行,通常三引号也可以起到注释的作用
# ３．可以用反斜杠来换行,或者用三引号
# ４．位置传参，关键字传参，命名关键字传参，*args星号元祖传参,**keargs双星号字典传参，引用传递
# ５．6 7 8
# ６．lambda x,y=3 : x*y 
# ７．[x for x in range(1,100) if x % 3 == 0 ]
# ８．try-except try-finally
# ９．__init__是初始化 ,当实例化时一定会调用此函数 , __ new__ 是创建并返回一个对象
# １０．LEGB 四个优先级 L:局部 E外部嵌套函数作用于,G:全局作用域,B系统内建作用域

# 四.
'''
def f(n):
    x = 0
    if n == 1:
        return 1
    x = n * f(n-1)
    return x

print(f(5))
'''
'''
# 遍历多层列表
def fun(L):
    for l in L:
        if type(l) is int :
            print(l)
        elif type(l) is list:
            fun(l)
l = [1,2,3,4,5,[67,8,[1,8,9],9]]
fun(l)
'''













# AID第一阶测试试卷
# 一、单选题（6*2=12）
# 1、for x in range(5,0,-2):
#        print(x)
#    打印结果是？（）
#    A  4
#       2
#       0
#    B  5
#       3
#       1
#    C  0
#       2
#       4
#    D  1
#       3
#       5
# 2、有如下代码：
#    a = {“one”:1,”two”:2,”three”:3}
#    a[“one”] += 1
#    print(a[“one”])
#    执行结果是？（）
#    A  1
#    B  2
#    C  None
#    D  有语法错误不能执行
# 3、有字典：d={“a”:3,”b”:2,”c”:1}，以下表达式为True的是?（）
#    A  3 in d
#    B  (“a”,3) in d
#    C  “b” in d
#    D  bool(d.clear())
# 4、S=”ABCDEFG”则S[-2:-5]得到的字符串对象是？（）
#    A  CDEF
#    B  FEDC
#    C  FED
#    D  “”
# 5、执行代码：
#    L = [1,2,3]
#    def func(a):
#        a = [4,5,6]
#    func(L)
#    print(L)
#    A  [1,2,3]
#    B  [4,5,6]
#    C  1,2,3
#    D  4,5,6
# 6、有字典：d = {“a”:3,”b”:2,”c”:1},sorted(d)得到的是？（）
#    A  {“a”:3,”b”:2,”c”:1}
#    B  {“c”:1,”b”:2,”a”:3}
#    C  [1,2,3]
#    D  [“a”,”b”,”c”]
# 二、多选题（6*3=18）
# 1、关于python字符串，下列说法正确的是？（）
#    A  python字符串属于不可变类型
#    B  python字符串属于python序列类型
#    C  python字符串索引不能为负
#    D  python字符串支持切片操作
# 2、python3交互模式下，执行如下代码：
#    L1 = [1,2,3]
#    L2 = [L1,4,5]
#    L3 = L2
#    L4 = L3.copy()
#    L1[1] = 10
#    L3[1] = 40
#    L4[2] = 50
#    以下说法正确的是？（）
#    A  L2的值为：[[1,10,3],40,5]
#    B  L3的值为：[[1,10,3],40,5]
#    C  L4的值为：[[1,2,3],4,50]
#    D  L4的值为：[[1,10,3],4,50]
# 3、关于python集合下列说法正确的是？（）
#    A  集合内的元素必须是不可变对象
#    B  集合是可迭代的
#    C  集合内元素不能重复
#    D  True 和 None都可以作为集合内的元素
# 4、关于python的if语句下列说法正确的是？（）
#    A  if 语句必须有 ：
#    B  if 语句必须有else分支
#    C  if语句必须有可求值的条件表达式
#    D  if语句可以有elif分支，else分支必须放最后
# 5、以下执行不会报错的是（）
#    class A:
#     def __init__(self):
#         self._a = 100
#         self.__b = 200
#         self.__c_ = 300
#         self.__d__ = 400
# a = A()
# A  print(a._a)
# B  print(a.__b)
# C  print(a.__c_)
# D  print(a.__d__)
# 6、以下说法正确的是（）
# A  实例方法只能用实例来调用
# B  类方法用实例和类都可以调用
# C  静态方法只能用类来调用
# D  静态方法用实例和类都可以调用
# 三、解答题（10*5=50）
# 1、有列表 name = ['P', 'y', 'h', 'o', 'n']，如果我想要在元素 'y' 和 'h' 之间插入元素 't'，应该使用什么方法来插入？
# 2、单引号，双引号，三引号的区别？
# 答：
# 3、如何定义一个跨越多行的字符串吗（请至少写出两种实现的方法）？
# 答：
# 4、Python函数参数传递的几种形式，并说明函数传参是值传递还是引用传递？
# 答：
# .
# 5、以下是“闭包”的一个例子，请你目测下会打印什么内容？
#    def funX():
#        x=5
#        def funY():
#            nonlocal x
#            x += 1
#            return x
#        return funY
# a = funX()
# print(a())
# print(a())
# print(a())
# 6、请使用lambda表达式将下面的函数转变为匿名函数
#    def fun_A(x,y=3):
#        return x*y
# 7、使用列表推导式快速求出100以内所有3的倍数。
# 答：
# 8、我们使用什么方法来处理程序中出现的异常？

# 9、__init__ 和 __new__ 的区别？
# 答：
# 10、Python中的作用域以及优先级？
# 答：
# 四、编程题（2*10=20）
# 1、利用递归方法求5!。
# 答： 

# 2、有一个多层嵌套的列表 A = [1,2,[3,4,[‘434’,[…]]]],请写一段代码遍历A中的每个元素并打印出来


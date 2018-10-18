# 补充
1. globals() 函数和 locals  函数
    - globals() 返回当前全局作用域内变量的字典
    - locals()  返回当前局部作用域内变量的字典
    - 示例 lx0

2.  函数变量
    - 函数名是变量,他在创建函数时绑定一个函数
    - 示例lx1\lx2

3. 一个函数可以作用另一个函数的实参传递
    - 可以把一个函数给另一个函数,另一个函数的形参变量将绑定实参函数
    - 示例lx3 lx4
4. 函数可以作为另一个函数的返回值
    - 示例 lx5_return_function.py
- 练习: 写一个计算公式的执行器
5. 函数的嵌套定义
- 函数嵌套定义时指一个函数里用def语句来创建其它函数的情况
- 示例 lx7

# python 的作用域/命名空间
- 是访问变量时查找变量的名范围空间
## 一共四个作用于 LEGB
作用域| 英文解释 | 英文缩写
---|---|---
局部作用域|Local(function)|L
外部嵌套函数作用域|Enclosing Fucntion local| E
函数定义所在模块(文件)的作用域|Global(module)|G
python内建模块的作用域|Builtin(python)|B
- 变量名的查找规则 L-->E-->G-->B
- 注: 在默认的情况下,变量名赋值会创建或改变当前作用域内变量的绑定关系

# global 语句
## 作用
- 告诉解释执行器,global语句声明的一个或者多个变量,这些变量的作用于为模块级的作用域,也称作全局变量
- 全局生命(global)讲赋值语句的变量映射到模块文件内部的作用域
## 语法:
- `global 变量名1, 变量名2......
## 示例
- lx8_global.py
## 说明<font color=FFF444>
- 全局变量如果在函数内部被赋值,则必须通过全局变量生明(否则会被认为是局部变量)
- 全局变量在函数内部不经过声明就可以直接访问(取值)
- 不能先创建局部变量,再用global生明为局部变量,此种做法不符合规则
- global变量列表里的变量名不能出现在函数的形参列表里,否则出错</font>

# nonlocal 语句
## 作用
- 告诉解释器,nonlocal神明的变量不是局部变量,也不是全局变量.而是外部嵌套函数内的变量
## 语法
- nonlocal 变量名1,变量名2,...
##示例
```py
c = 100
def A():
    c=50
    print(c)
    def B():
        #加nonlocal
        nonlocal c
        c = 25
        print(c)
    B()
    print(c)
A()
print("quanjv", c)
# out :50
# 25
# 25
# quanjv 100
```
## 说明<font color=FFF699>
- nonlocal 语句只能在被嵌套函数内部进行使用
- 对nonlocal变量进行赋值讲对外部嵌套函数作用于内的变量进行操作
- 当有两层或者两层以上的函数嵌套时,访问nonlocal变量只对最近一层的一层变量进行操作
- nonlocal 语句的变量列表里的变量名不能出现在此函数的形参的形参列表中</font>

# lanbda 表达式(又称匿名函数)
## 作用
- 创建一个匿名函数对象
- 同def 类似但不提供函数名
## 语法
- `lambda [函数型参列表]: 表达式`
## 示例:
    - lx10_lambda.py
## 注意<font color = 877FFF>
- lambda 直接返回的是:后面的值,等同于def里的return 示例:lx10.py
- lambda 表达式时创建的函数只能包含一条表达式
- lambda 比函数简单,且可以随时创建和销毁,有利于降低程序的耦合度
- lambda 赋值就是直接在后面加括号传实参</font>



# eval() 函数 和 exec() 函数
## eval(source,global=None, local = None) 
- 把一个字符串source 当成一个表达式来执行,返回表达式执行结果
## exec(source , global = None , local = None)
- 把一个字符串source 当成一个程序来执行

```py
s= "1 + 2 * 3 + 4"

v = eval(s)
print(v)  # 11

while True:
    s = input(">>> ")
    print(eval(s))




s= "x + y"

d1 = {"x":100, 'y':200}
d2 = {"x":1}
# d1 传入 代表的时全局变量
# d2 传入 代表的是局部变量
v = eval(s, d1, d2)
# 所以x == 1
print(v)




s = '''
myadd = lambda x, y: x + y

print("20+30=", myadd(20, 30))  # 50
print("4 + 5 =", myadd(4, 5))  # 9
'''

exec(s)
```
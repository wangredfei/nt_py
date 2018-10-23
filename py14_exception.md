# 异常 exception(基础)

## 什么是错误
- 错误是指由于逻辑或语法等导致程序无法执行的问题
- 特点 
    - 无法预知

## 什么时异常
- 异常是程序出错时标识的一种状态.当异常发生时,程序不会再向下执行,而转去调用此函数的地方处理此错误并恢复为正常状态
- 作用
    - 用作信号通知,通知上层调用者有作物产生需要处理
## 程序有两种状态
- 正常状态/异常状态

## try 语句的两种语法
- try-except 语句
- try-finally 语句
### try-expect 的语法
```py
try :
    可能出发异常的语句
except 错误类型1 [as 变量名1]:
    异常处理语句1
except 错误类型2 [as 变量名2]:
    异常处理语句2
except (错误类型3,错误类型4) [as 变量名3]:
    异常处理语句3
...
except:
    异常处理语句 other
else :
    未发生异常的语句
```
- 作用
    - 尝试捕获错误,得到异常通知,将程序由异常状态转换为正常状态并继续执行
- 说明
    - as字句是用于绑定错误对象的变量,可以省略
    - except 字句可以有一个或者多个,但至少要有一个 , 必须放在最后
    - else 字句最多只能有一个,也可以省略
    - finally字句最多只能有一个,也可以省略

### try - finally 语句
- 语法
    ```py
    try:
        可能触发异常的语句
    finally:
        最终语句
    ```
- 说明
    - finally 不可以省略
    - 一定不存在except子句
- 作用
    - 通常用try-finally 语句来做触发一场时必须要处理的事情,无论异常是否发生,finally都会被执行
- 注意
    - try-finally语句不会改变程序的(正常\异常)状态
    



## python中全部的错误类型
错误类型 |	说明
---|---
ZeroDivisionError |	除(或取模)零 (所有数据类型)
ValueError 	|传入无效的参数
AssertionError |	断言语句失败
StopIteration |	迭代器没有更多的值
IndexError 	|序列中没有此索引(index)
IndentationError 	|缩进错误
OSError 	|输入/输出操作失败
ImportError 	|导入模块/对象失败
NameError |	未声明/初始化对象 (没有属性)
AttributeError |	对象没有这个属性
GeneratorExit 	|生成器(generator)发生异常来通知退出
TypeError 	|对类型无效的操作
KeyboardInterrupt |	用户中断执行(通常是输入^C)
OverflowError |	数值运算超出最大限制
FloatingPointError |	浮点计算错误
BaseException |	所有异常的基类
SystemExit |	解释器请求退出
Exception 	|常规错误的基类
StandardError |	所有的内建标准异常的基类
ArithmeticError |	所有数值计算错误的基类
EOFError 	|没有内建输入,到达EOF 标记
EnvironmentError 	|操作系统错误的基类
WindowsError |	系统调用失败
LookupError |	无效数据查询的基类
KeyError 	|映射中没有这个键
MemoryError |	内存溢出错误(对于Python 解释器不是致命的)
UnboundLocalError 	|访问未初始化的本地变量
ReferenceError| 	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError 	|一般的运行时错误
NotImplementedError |	尚未实现的方法
SyntaxError Python |	语法错误
TabError 	|Tab 和空格混用
SystemError |	一般的解释器系统错误
UnicodeError |	Unicode 相关的错误
UnicodeDecodeError |	Unicode 解码时的错误
UnicodeEncodeError |	Unicode 编码时错误
UnicodeTranslateError |	Unicode 转换时错误
以下为警告类型 	|
Warning |	警告的基类
DeprecationWarning| 	关于被弃用的特征的警告
FutureWarning |	关于构造将来语义会有改变的警告
OverflowWarning |	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning |	关于特性将会被废弃的警告
RuntimeWarning |	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning |	可疑的语法的警告
UserWarning 	|用户代码生成的警告



# raise 语句
- 作用
    - 触发一个错误,让程序进入异常状态
    - 发送错误通知给调用者
- 语法
    - raise 异常类型
    - raise 异常对象
    - raise   # 重新出发上一次异常
- 示例 lx6

# assert 语句
- 语法
    - assert 真值表达式, 错误数据(通常是字符串)
- 作用
    - 当真值表达式为False时,用错误数据创建一个AssertionRttor类型的错误,  
    并进入异常状态,通常用故意制造一个错误
- 等同于 
    ```py 
    if bool(真值表达式) == False:  
        raise AssertionError(错误数据)
    ```

# 总结一下异常中的语句
- try-except 用于捕获(接受)错误通知,把异常状态转为正常状态
- try-finally 用于执行在任何状态(正常\异常)都必须要执行的语句
- raise 用于触发错误(发送错误通知),让程序进入异常状态
- assert 根据条件触发AssertionError类型的错误通知


# 迭代器 Iterator
- 什么是迭代器
    - 迭代器时访问可迭代对象的工具
    - 地带其实指iter(obj)函数返回的对象(实例)
    - 迭代器可以用next(it) 函数获取可迭代对象的数据
## 迭代器函数 iter 和 next
- iter(iterable) 
    - 从可迭代对象中获取一个迭代器, iterable必须是能提供一个迭代器的可迭代对象
- next(Iterator) 
    - 从迭代器Iterator中获取下一个记录,如果无法获取吓一跳记录,则出发StopIteration异常
- 说明
    - 迭代器只能往前取值,不会后退
    - 用iter函数可以返回一个可迭代对象的迭代器

# 作业
1. 一个球从100米高空下落,每次落地后反弹高度为原高度
的一半,再落下,写程序:
    1) 算出皮球在第10次落后反弹多高
    2) 算出皮球在第10次反弹后经过多少米路程

2. 分解质因数.输入一个正整数,分解质因数
如 输入: 90 则打印: 90=2*3*3*5
(质因数是指最小能被原数整除的素数(不包括1))

3. 修改原学生信息管理程序,加入异常处理语句,让程序
在任何情况下都能按逻辑正常执行.
    如输入成绩,年龄等都不会导致程序崩溃

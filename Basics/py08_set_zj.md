# 集合 set
## 概念 
- 是可变的容器   
- 集合内的对象都是唯一的(不能重复多次的)
- 集合时无序的存储结构,集合中的数据没有先后关系
- <font color = 999FFF >集合内的元素必须是不可变的对象</font>
- 集合时可迭代的(可以用for遍历)
- 集合相当于只有键没有值的字典(键则是集合的数据)
## 创建集合的构造函数
- set()     创建一个空的集合对象(不能用{}来创建空集合)  
创建空集合的唯一方式  
`s = set() # s绑定空集合`
- set(iterable) 用可迭代对象来创建新的集合对象  
`s = set(range(1,5)) out:{1,2,3,4}`  
`s = set("hello")    out:{"h","e","l","o"}`
- 字面值方式来创建非空集合  
`s = {1,2,3,4}`
- 注:非空集合用{}括起来,内部的各个元素用逗号隔开    
```python
s = set({1:"yi",2:"er",3:"three"})  # out :{1,2,3}]
s = set([1,2,3,4]) #out:{1,2,3,4}
s = {True, None, "ABC", [1,2,3]} # 会出错因为列表时可变的
```

## 集合的运算
- 交集 &  
  并集 |  
  补集 -   
  对称补集 ^  
  子集 <  
  超集 >  

- 交集 &  生成两个集合的交集
```python
s1 = {1,2,3}
s2 = {2,3,4,5}
s1 & s2
# {2, 3}
```
- 并集 | 
```python
s1 = {1,2,3}
s2 = {2,3,4,5}
s1 | s2
# {1,2,3,4}
```

- 补集 - 
```python
s1 = {1,2,3}
s2 = {2,3,4,5}
s3 = s1 - s2 # 生成属性s1但不属于s2的所有元素的集合
# s3 = {1}
s1 = {1,2,3}
s2 = {2,3,4,5}
s3 = s2 - s1
# s3 = {4}
```
- 对称补集 ^
```python
s1 = {1,2,3}
s2 = {2,3,4,5}
s3 = s1 ^ s2
# s3 = {1,4,5}
```
- 子集 <  
超级 >  
```python
s1 = {2,3}
s2 = {2,3,4,5}
s3 = {1,2,3}
s1 < s2  # True   
s3 < s2  # Flase

```
- 包含不包含的关系，　不是比较大小


## in \not in 
－　等同于列表

#＃　集合和字典的优点
－　in \ not in 运算符的运算速度比较快

##　能用于集合的内建函数
-   len(x)  
    max(x)  
    min(x)  
    sum(x)  
    any(x)  
    all(x)  

## python3中常用的集合方法
方法 |	意义
---|---
S.add(e) 	|在集合中添加一个新的元素e；如果元素已经存在，则不添加
S.remove(e) 	|从集合中删除一个元素，如果元素不存在于集合中，则会产生一个KeyError错误
S.discard(e) |	从集合S中移除一个元素e,在元素e不存在时什么都不做;
S.clear() |	清空集合内的所有元素
S.copy() 	|将集合进行一次浅拷贝
S.pop() 	|从集合S中删除一个随机元素;如果此集合为空，则引发KeyError异常
S.update(s2) 	|等同于 S l= s2, 用 S与s2得到的全集更新变量S
S.difference(s2) |	S - s2 补集运算，返回存在于在S中，但不在s2中的所有元素的集合
S.difference_update(s2) |	等同于 S -= s2
S.intersection(s2) |	等同于 S & s2
S.intersection_update(s2) |	等同于S &= s2
S.isdisjoint(s2) |	如果S与s2交集为空返回True,非空则返回False
S.issubset(s2) |	如果S与s2交集为非空返回True,空则返回False
S.issuperset(...) |	如果S为s2的子集返回True,否则返回False
S.symmetric_difference(s2) |	返回对称补集, 等同于 S ^ s2
S.symmetric_difference_update(s2) |	等同于 S ^= s2, 用 S 与 s2 的对称补集更新 S
S.union(s2) |	生成 S 与 s2的全集, 等同于 S \

## <font color = 999FFF >注意: 集合是可迭代对象 </font>

## 集合推导式
- 含义
    - 集合推导式是用可迭代对象创建集合的表达式
- 语法
    - {表达式 for 变量 in 可迭代对象 [if 真值表达式]}
- 集合推导式的嵌套
    - 等同于列表
### 推导式的作用是在创建容器的时候把数据放进去

# 比较
可变的|不可变的
---|---
list|tuple
dict|str
set|frozenset

# 固定 frozenset
- 含义
    - 去重,含有唯一元素的集合
- 作用
    - 固定集合可以作为字典的键,还可以作为集合的值
    - 去重
- 固定集合的构造函数
    - frozenset()    创建一个空的固定集合
    - frozenset(iterable) 用可迭代对象创建一个固定集合font

- 示例
    ```python
    fz = frozenset()
    fz = frozenset("AB")
    fz = frozenset(range(5))# out: frozenset({0, 1, 2, 3, 4})
    ```
##　固定集合的运算
- 交集 &   
并集 |   
补集 -   
对称补集 ^
子集 < >
- in not in 运算符
-  < <= > >=  
## 固定集合的方法, 等同于集合的方法去掉修改集合的方法



# 阶段性总结:
## 数据类型
不可变|可变的
---|---
bool    | list
int     | dict
float   | set
complex |bytearray
str     |
tuple   |
frozenset|
bytes(字节串)|

## 值
- None , False , True
## 运算符l
- ```+ - * / // % **  
    < <= > >= == !=  
    in not in   
    not  and or  
    & | ^  
    +  - 
    [:] # 索引和切片
## 表达式:
- 1   
 True   
 1+2*3   
函数调用:print("hello")  
方法  
内建函数  
条件表达式  
-  全部的推导式
    - 列表  
    字典  
    集合  
    <font color = 999FFF >只有三种</font>
## 语句  
- 表达式语句(表达式单独在一行可以形成表达式语句)
    - print("hello")
- 赋值语句
    - a = 100
- del  
- if  
- while  
- for  
- break  
- continue-   
- pass
## 函数
- len(x) , max(x) , min(x) , any(x) , all(x)
- bool(x) , str() ,liat(),dict(),tuple(),set(), frozenset()
- abs(x) ,round() , pow(x,y,z= None)
- bin(x) ,oct(x), hex(x), chr(x) , ord(x)
- range(start,shop,step)
- 基本输入输出 input print
- id(x),type(x)


# 函数  function
## 含义
- 函数是乐意重复执行的语句块,可以重复调用并执行函数的面向过程编程的最小单位
## 作用
- 用于封装语句块,提高代码重读性
- 定义用户级别的函数
- 提高代码的可读性和易维护性
## def 语句
### 语法
 ```
 def 函数名(形参列表):  
    语句块
```
- 作用
    - 创建一个函数,将语句块打包,用函数名绑定,用来调用
- 说明
    - 函数名的明明规则与变量的明明规则相同(必须为标示符)
    - 函数名是一个变量,用来绑定函数
    - 函数有自己的名字空间,在函数外部不可以访问函数内内部的变量,在函数内部可以访问函数外部的变量,但不能对外部的变量赋值
    - 语句部分不能为空,如果为空需要填允pass语句
    - 函数如果不需要传入参数,形参列表可以为空
### 函数调用
- 语法
    - 函数名(实际调用传递参数)
- 说明
    - 函数调用是一个表达式
    - 如果函数内部没有return语句,函数执行完毕后返回None对象的引用
- 示例
    - lx2
## return 语句
- 语法
    - return  [表达式]
    - 注: []代表其中内容可以省略
- 作用:
    - 用于函数中,结束当前函数的执行,返回到调用该函数的地方,同时返回一个对象的引用关系
- 说明
    1. return 语句后跟的表达式可以省略,省略后相当于return None
    2. 函数内部没有return语句,则函数执行完最后一条语句后返回None(相当于在最后加了一条return语句)
- 示例
    - 见lx5
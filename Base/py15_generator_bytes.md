# 生成器Generator
- 生成器时能够动态提供数据的可迭代对象
- 生成器在程序运行时升成数据,与容器类不同,它通常不会在内存中保存大量的数据,现用现生成

## 好处
- 不占用计算机的内存
## 生成器有两种
- 生成器函数
- 生成器表达式
## 生成器函数的定义
- 含有yield语句的函数时生成器函数,此函数被调用将返回一个生成器对象
- yield 翻译为(产生和生成)

### yield 语句
- 语法
    - yield 表达式
- 说明
    - yield 只能用于def函数中,目的是将此函数作为生成器函数使用
    - yield用来生成数据,供迭代器的next(it) 函数使用
- 示例 lx1

- 说明
    - 生成器函数的调用将返回一个生成器对象,生成器对象是一个可迭代对象
    - 生成器函数用return会触发一个StopIteration异常(即生成结束)
    - 生成器对象是一次性的(gen = 生成器()),gen一旦生成结束以后,将不能再重新生成数据
## 生成器表达式
- 语法:
    - `(表达式 for 变量 in 可迭代对象 [if 真值表达式])`
- 作用
    - 用推导式形式创建一个新的生成器
- 说明
    - if子句可以省略
    - 生成器表达式也可以向列表推导式一样嵌套

# 迭代工具函数
- 迭代工具函数的作用是生成一个符合条件的可迭代对象
## zip(iter1[,iter2[,iter3[,.....]]])  
- 返回一个zip生成器对象,此对象用于生成一个元组,  
    此元组的数据分别来自于参数中的每个可迭代对象,  
    生成元组的个数由最想的一个可迭代对象决定
```py
a = [1,2,3,4,5,6,7]
b = ['a','b','c','d', 'e','f','g']
for i in zip(a,b,range(10)):
    print(i)
# (1, 'a', 0)
# (2, 'b', 1)
# (3, 'c', 2)
# (4, 'd', 3)
# (5, 'e', 4)
# (6, 'f', 5)
# (7, 'g', 6)
c = dict(zip(a,b))
print(c)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g'}
```
## enumerate(iterable, start = 0) 
- 返回一个numberate 生成器对象,  
  此对象生成类型为(索引,值对)的元组默认索引从零开始,  
   也可以用start指定
```py
a = [1,2,3,4,5,6,7]
b = ['a','b','c','d', 'e','f','g']
for i in enumerate(b,start = 65):
    print(i)
# (65, 'a')
# (66, 'b')
# (67, 'c')
# (68, 'd')
# (69, 'e')
# (70, 'f')
# (71, 'g')
```

# 字节串(字节序列) bytes
- 存储以字节为单位的数据
- 字节串是不可变的字节序列
- 说明
    - 字节时0~255之间的整数,用来表示一个字节的取值
- 创建空字节的字面值方式
    - b''
    - b""
    - b''''''
    - b""""""
- 创建非空字节串的字面值
    - b'ABCD'
    - b"ABC"
    - b'''aaaa'''
    - b"""BBBB"""
- 字节串的构造函数 bytes
    - bytes() 生成一个空的字节串,等同于b''
    - bytes(整数可迭代对象) 用可迭代对象初始化一个字节串
    - bytes(整数n) 生成n个值为0的字节串
    - bytes(字符串,encoding='utf-8') 用字节串转换编码生成一个字节串 
- 示例
```py
B = bytes()
B = bytes(range(0x41,0x61))
B = bytes([65,66,67,68])
B = bytes(10)
B = bytes('hello','utf-8')
```
## 字节串的运算
` +    += *  *=  `  
`<   <=   >  >=  == !=  `  
`in  not in `   
` 索引  切片 `    
`
- 函数:
    - len(x) , max(x) , min(x ) ,sum(x), any(x),all(x)

## bytes 与 str去区别
- bytes 存储字节(0~255之间的整数)
- str 存储 UNICODE 字符(0~0x10FFFF)的字符

## bytes与str的转换
- str -----> bytes
    - b = s.encode(encoding='utf-8')
- bytes -----> str
    - s = b.decode(encoding='utf-8')
- exanple
```py
s= 'ABC中文'
b = s.encode("utf-8")
s2 = b.decode("utf-8")
print(s,b,s2)
```


# 字节数数组 bytearray 
- 可变的字节串
## 只有构造函数
- bytearray()
- bytearray(整形可迭代对象)
- bytearray(整数n)
- bytearray(字符串,encoding = 'utf-8')
## 运算同bytes
## 方法
方法|解释
---|---
B.clear() |	清空
B.append(n) |	追加一个字节(n为0-255的整数)
B.remove(value) |	删除第一个出现的字节,如果没有出现，则产生ValueError错误
B.reverse() |	字节的顺序进行反转
B.decode([encoding='utf-8']) 	| 解码
B.find(sub[, start[, end]]) | 查找

# 练习:
1. 写一个生成器函数myxrange([start,]stop[,step])  
    来生成一系列的整数  
要求myxrange功能与range函数功能完全相同  
(不允许调用range函数和列表)   
用自己写的myxrange,结合生成器表达式求 100以内所  
有的奇数的平方和  

2. 写一个生成器函数fibonacci, 生成斐波那契数的前n个数  
    1 1 2 3 5 8 ....  
    如:  
    ```
        def fibonacci(n):  
            ...
            yield ...
            ...
    ```
      1) 打印前20个数:  
        for x in fibonacci(20):  
            print(x)
      2) 打印前40个斐波那契数的和  
        print(sum(fibonacci(40))) 
 

3. 思考题:  
     如何让学生管理系统启动时就能读取文件中的信息来加载
     数据?  (预习文件操作)
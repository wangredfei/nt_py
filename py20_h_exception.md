# with 语句
- 语法
    ```py
    with 表达式1 [as 变量1], 表达式2[as 变量2],..... :
        语句块
    ```
- 作用
    - 适用于对资源进行访问的场合,确保使用过程中不管是否发生异常,都会去执行必须的'清理'操作,并释放资源
    - 如:
        - 文件使用后自动关闭,县城中锁的自动获取和释放等
- 说明
    - 执行表达式,用as 子句中的变量绑定生成的对象with语句并不改变异常的状态
- lx0


# 环境管理器
- 类内有 `__enter__` 和 `__exit__`示例方法的类被称为环境管理器
- `__enter__`
    - 将在进入with语句时被调用,并返回由as变量管理的对象
- `__exit__` 
    - 将在离开with语句时被调用,且可以用参数来判断在离开with语句时是否有异常发生,并做出相应的处理
- 不会的时候去看!!-->`lx1`


# 运算符重载
- 让自定义的类生成的对象(实例)能够使用运算符进行操作
- 作用
    - 让自定义的类的实例像内奸对象一样使用运算符
    - 让程序简洁易读
    - 对自定义的对象将运算符赋予新的运算规则
- 算术运算符重载
- 
    方法名|运算符和表达式|说明
    ---|---|---
    `__add__`(self,rhs)|self+rhs|加法
    `__sub__`(self,rhs)|self-rhs|减法
    `__mul__`(self,rhs)|self*rhs|乘法
    `__truediv__`(self,rhs)|self/rhs|除法
    `__floordiv__`(self,rhs)|self//rhs|地板除
    `__mod__`(self,rhs)|self%rhs|求余
    `__pow__`(self,rhs)|self**rhs|幂运算
- 说明
    - 运算符重载的方法的参数已经有固定的含义,不建议改变原的意义

# 反向算术运算符的重载
- 当运算符左侧为内建类型,右侧为自定义类型进行算术运算时,会出现Typeerror错误
- 因无法修改内建类型的代码来实现运算符重载,此时需要使用反向运算符重载来完成重载
- 
    方法名|运算符和表达式|说明
    ---|---|---
    `__radd__`(self,lhs)|lhs + self|加法
    `__rsub__`(self,lhs)|lhs - self|减法
    `__rmul__`(self,lhs)|lhs * self|乘法
    `__rtruediv__`(self,lhs)|lhs / self|除法
    `__rfloordiv__`(self,lhs)|lhs //self|地板除
    `__rmod__`(self,lhs)|lhs % self|求余
    `__rpow__`(self,lhs)|lhs** self|幂运算

# 复合赋值算术运算符重载
- 以复合赋值运算符`x += y为例`,此运算符会优先调用`x.__iadd__(y)` 方法,如果没有__iadd__方法时会讲符合赋值运算符拆解为` x = x+y` 然后再调用`x = x.__add__(y)`方法,如果再不存在__add__方法则会触发TypeError异常
- 其他复合赋值运算符也具有相同的规则

    方法名|运算符和表达式|说明
    ---|---|---
    `__iadd__`(self,rhs)|self += rhs|加法
    `__isub__`(self,rhs)|self -= rhs|减法
    `__imul__`(self,rhs)|self *= rhs|乘法
    `__itruediv__`(self,rhs)|self /= rhs|除法
    `__ifloordiv__`(self,rhs)|self //= rhs|地板除
    `__imod__`(self,rhs)|self %= rhs|求余
    `__ipow__`(self,rhs)|self **= rhs|幂运算

# 比较运算符的重载
方法名|运算符和表达式|说明
---|---|---
`__lt__(self,rhs)` | self < rhs | 小于
`__le__(self,rhs)` | self <= rhs | 小于等于
`__gt__(self,rhs)` | self > rhs | 大于
`__ge__(self,rhs)` | self >= rhs | 大于等于
`__eq__(self,rhs)` | self == rhs | 等于
`__ne__(self,rhs)` | self != rhs | 不等于

- 注
    - l :little
    - e :equal
    - g :greater
    - t :than



# 位运算符重载:
方法名|运算符和表达式|说明
---|---|---
 `__and__(self, rhs) ` |  self &  rhs  |  位与
 `__or__(self, rhs)  ` |  self |  rhs  |  位或
 `__xor__(self, rhs) ` |  self ^  rhs  |  位异或
 `__lshift(self, rhs)` |  self << rhs  |  左移
 `__rshift(self, rhs)` |  self >> rhs  |  右移

# 反向位运算符重载:
方法名|运算符和表达式|说明
---|---|---
 `__rand__(self, lhs)  `| lhs &  self  |   位与
 `__ror__(self, lhs)   `| lhs |  self  |   位或
 `__rxor__(self, lhs)  `| lhs ^  self  |   位异或
 `__rlshift(self, lhs) ` |lhs << self  |   左移
 `__rrshift(self, lhs) `| lhs >> self  |   右移

# 复合赋值位运算符重载:
 方法名|运算符和表达式|说明
---|---|---
 `__iand__(self, rhs) `   self &=  rhs    位与
 `__ior__(self, rhs)  `   self |=  rhs    位或
 `__ixor__(self, rhs) `   self ^=  rhs    位异或
 `__ilshift(self, rhs)`   self <<= rhs    左移
 `__irshift(self, rhs)`   self >>= rhs    右移

# 一元运算符的重载
方法名|运算符和表达式|说明
---|---|---
 `__neg__(self)  ` |  - self   |   负号
 `__pos__(self)   `|  + self   |   正号
 `__insert__(self) `| ~ self   |   取反

- 语法:
```py
   class 类名:
       def __xxx__(self):
           ....
```


- in / not in 运算符重载
       方法名       |      运算符和表达式
       ---|---
 `__contains__(self, e)`  |  e in self    



- 索引和切片运算符的重载
-   L[0]
-   L[::2]
 方法名|运算符和表达式|说明
---|---|---
 `__getitem__(self, i)    `|  x = self[i] | 取值
 `__setitem__(self, i, v) `|self[i] = v | 赋值
 `__delitem__(self, i)    `| del self[i] | 删除索引


  

# slice 构造函数
- 作用:
    用于创建一个slice切片对象,此对象存储一个切片
    的起始值,终止值和步长信息,默认都为None
- 格式:
    slice(start=None, stop=None, step=None)
- slice对象的属性
    s.start 切片的起始值 默认为None
    s.stop  切片的终止值,默认为None
    s.step  切片的步长,默认为None
- 示例见:
    lx4_mylist_slice.py

# 特性属性 @property
- 实现其它语言所拥有的 getter 和 setter 功能

- 作用:
    - 用来模拟一个属性
    - 通过@property装饰器可以对模拟的属性赋值和取值加以控制
- 示例见:property.py













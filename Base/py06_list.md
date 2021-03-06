# 继续列表
## 列表的比较运算
- 运算符
    - < <= > >= == !=
- 说明
    - 列表的比较规则与字符串的比较规则相同
    - 列表要求每两个元素依次进行比较，否则会出现类型错误
- 示例
    ```python
    [1, 2, 3] < [1, 2, 4] #True
    [1, 2, 3] != [1, 2, 4] #True
    ["one", "two"] < ["1", "2"] #True
    ["two", 1] < [1, "two"] #TypeError
    ```
## 列表的in 、not in运算符
- 判断一个值是否存在列表中，如果存在则返回True ， 否则 Flase
- 同字符串的 in 运算符类似
- 示例
    ```python
    x = [1, 'two', 3, "四"]
    3 in x          # True        
    "3" in x        # Flase
    10 not in x     # Flsae
    ```
## 列表索引操作：
### 索引取值语法：
- x = 列表[整数表达式]
- 用法
    - 等同于字符串的索引（同样分为正索引反索引）
### 索引赋值
- 列表时可变的列表，可以通过索引赋值改变列表中的元素
- 语法
    - 列表[整数表达式] = 表达式
- ```python
    x = [1, 2, 3, 4] 
    x[2] = 3.14
    print(x)
    # out: [1, 2, 3.14, 4]
    # 此时id不变
    x = "1234"
    x[2] = 3.14
    print(x)
    # TypeError 因为字符串时不可变的
    ```
## 列表的切片操作
### 切片取值
- 列表[起始索引：终止索引：步长]
- 列表的切片取值是从原列表中取出想要色元素再次组成一个新的列表
- 一定得到时时一个列表
### 切片赋值
- 可以改变源列表的排列，可插入，可修改数据
- 说明
    - 列表[切片] = **可迭代对象**
    ```python
    L = [2, 3, 4]
    L[0:1] = [1.1, 2.2]  # L=[1.1, 2.2, 3, 4]
    L[0:2] = [2]  # L = [2, 4]
    L[1:2] = [3.1, 3.2]  # L = [2, 3.1, 3.2, 4]

    L = [2, 3, 4]
    L[1:1] = [2.1, 2.2]  # L = [2, 2.1, 2.2, 3, 4]
    L[0:0] = [0, 1]  # L = [0, 1, 2, 2.1 ....]
    L = [2, 3, 4]
    L[3:3] = [5, 6]  # L = [2, 3, 4, 5, 6]

    L = [2, 3, 4]
    L[1:2] = "AB" # L = [2, 'A', 'B', 4]
    L[1:3] = range(7, 10)  # L = [2, 7, 8, 9, 4]
    ```
#### 切片的注意事项
- 对于步长不等于1的切片赋值，赋值运算符的右侧的可迭代对象提供的元素的个数，一定要等于切片的切出的段数
    ```python
    l = [1, 2, 3, 4, 5, 6]
    ll[::2] = "ABC"    # out : ["A", 2, "B", 4, "C",6]
    ll[::2] = "ABCD"   # 错误，因为切片切出来三个，赋值四个
    ```
## del 语句
- 可用于栓出列表的元素
- 语法：
    - del 列表[索引]
    - del 列表[切片]
- 示例
    ```python
    L = [1, 2, 3, 4, 5, 6]
    del L[-1] # 6被删除了
    del L[1::2] # 2,4,6 被删除了
    ```
## 练习
1. 已经有列表：L = [3, 5]  
用索引颗切片操作，将原来列表改变为：  
L = [1, 2, 3, 4, 5, 6]  
将列表翻转：  
L = [6, 5, 4, 3, 2, 1]  
然后删除最后一个元素  
L = [6, 5, 4, ] 

- 见lx0_qp.py  

- 见lx1

## 常用于序列的函数
函数|说明
---|---
 len(x)   | 返回序列的长度
 max(x)   | 返回序列的最大值元素
 min(x)   | 返回序列的最小值元素
 sum(x)   | 返回序列中所有元素的和（元素必须是数字类型）
 any(x)   | 真值测试。如果列表中一个值为真值则返回True
 all(x)   | 真值测试。如果列表中有的值为真值则返回True


## 常用的列表方法
方法 |	意义
---|---
L.index(v [, begin[, end]]) |	返回对应元素的索引下标, begin为开始索引，end为结束索引,当 value 不存在时触发ValueError错误
L.count(x) 	|返回列表中元素的个数
L.copy() |	复制此列表（只复制一层，不会复制深层对象)
L.insert(index, obj) |	将某个元素插放到列表中指定的位置
L.append(x) |	向列表中追加单个元素
L.extend(lst) |	向列表追加另一个列表
L.remove(x) |	从列表中删除第一次出现在列表中的值
L.pop([index]) |	删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回删除元素的引用关系
L.clear() |	清空列表,等同于 L[:] = []
L.sort(reverse=False) |	将列表中的元素进行排序，默认顺序按值的小到大的顺序排列
L.reverse() |	列表的反转，用来改变原列表的先后顺序


### 注意
- ```python
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = l1
    l1.insert(3,"AA")
    print(l1) #l1 = [1, 2, 3, 'AA', 4, 5, 6]
    print(l2) #l2 = [1, 2, 3, 'AA', 4, 5, 6]
    # 是绑定关系
    l1.reverse()  # 反转　l1 的ｉｄ没变
    l1.sort(recerse=False) # 升序
    l1.sort(recerse=True) # 降序
    ```
#### 深拷贝 deep copy 和 浅拷贝 shallow copy
- ```python
    l =[1,2,3]
    l2 = l 
    # 不拷贝
    ```
- 浅拷贝
    - 浅拷贝是指在赋值过程中,只复制一层变量,不会复制深层变量绑定的对象的复制过程  
    ```python
    L = [3.1, 3.2]
    l1 = [1, 2, L]
    l2 = l1.copy()  #浅拷贝
    print(l1) # [1, 21 [3.1, 3.2]]
    print(l2) # [1, 21 [3.1, 3.2]]
    l2[2][0] = 3.14
    print(l1) # [1, 21 [3.14, 3.2]]
    print(l2) # [1, 21 [3.14, 3.2]]
    # 实质上 把L改变了 l1,l2并没有改变 ,里面绑定的是L变量
    ```
- 深拷贝
    ```python
    import copy  #导入复制模块
    L = [3.1, 3.2]
    l1 = [1, 2, L]
    l2 = copy.deepcopy(l1)  #deep拷贝
    print(l1) # [1, 21 [3.1, 3.2]]
    print(l2) # [1, 21 [3.1, 3.2]]
    l2[2][0] = 3.14
    print(l1) # [1, 21 [3.1, 3.2]]
    print(l2) # [1, 21 [3.14, 3.2]] 
    ```
# 列表与字符串区别
- 都是序列,元素之间有先后顺序关系
- 列表和字符串有相同的操作 : + += * *= < > in \not in
- **字符串是不可变化的序列,列表是可变的序列**
- 字符串的每个元素只能存储字符,而列表可以存储任意类型的元素
- 列表和字符串都是可迭代的对象


# 字符串的文本解析方法 split 和join
## `S.split(sep=None)`
- 将字符串使用spe作为分隔符分割字符串,返回分割后的字符串列表;当不给定参数时,用空白字符作为分割符
```python
s = 'Anfuwei is cool'
s.split()
L = ['Anfuwei','is','cool']

s = 'Anfuwei+is+cool'
s.split("+")
L = ['Anfuwei','is','cool']

```
## `S.join(iterable)`
- 用可迭代对象中的字符串生成一个中间用S进行分割的字符串
- 格式
    - `s = " ".join(可迭代对象)
```python
L = ['Anfuwei','is','cool']
s1 = "##".join(L)
#out : "Anfuwei##is##cool"
```
## 练习
- 有字符串"hello"
- 生成新的字符串:"h e l l o" 和"h-e-l-l-o"
```python
s = 'hello'
a = " ".join(s)
b = "-".join(l)
print(a)
# 'h e l l o'
print(b)
# 'h-e-l-l-o'
```
# 列表推导式 list comprehesion
## 含义
- 列表推导式时用可迭代对象创建列表的表达式
## 作用
- 创建列表
## 语法
-   [3表达式 for 2变量 in 1可迭代对象]  
    或者  
    [4表达式 for 2变量 in 1可迭代对象 if 3真值表达式]  

## 列表推导式的嵌套语句
- [4表达式 for 2变量 in 1可迭代对象 if 3真值表达式  
4表达式 for 2变量 in 1可迭代对象 if 3真值表达式]  



# 练习
1. 打印空心等边三角形
2. 用户简单登录
3. 有一些数字存于列表中,如:  L = [1, 3, 2, 1, 6, 4, 2, .....98, 82]
    - 将列表中出现的数字存入到另一个列表l2中
        - 要求 : 重复出现多次的数字只能在L2中保留一份(去重)
    - 将列表中出现两次的数字存于L3列表中,在L3列表中只保留一份
4. 生成一个列表,求 x 的平方+1的列表,跳过结果能被5整除的数, (注: 0 <= x <= 100)

5. 把 0 ~ 100 之 间的所有素数存于一个列表中  
    即: L = [2, 3, 5, 7, 11, ..... 97]

#　注意
```python
Ｌ＝　［１，　２，　３，　４，　５］
for i in L :
    L.remove(i)
print(L)
# out = [2, 4 ]  因为第一次删除１后２往前移动一位
```


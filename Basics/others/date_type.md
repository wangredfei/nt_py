不可变   | 可变的
---|---
bool    | list
int     | dict
float   | set
complex |bytearray
str     |
tuple   |
frozenset|
bytes(字节串)|

# 字符串方法
方法	|说明
---|---
S.isdigit()	|判断是否是数字
S.isalpha()	|判断字符串是否全为英文字母
S.islower()	|判断字符串所有字符是否全为小写英文字母
S.isupper()	|判断字符串所有字符是否全为大写英文字母
S.isspace()	|判断字符串是否全为空白字符
S.center(width[,fill])	|将原字符串居中，左右默认填充空格
S.count(sub[, start[,end]])	|获取一个字符串中子串的个数
S.find(sub[, start[,end]])	|获取字符串中子串sub的索引,失败返回-1
S.strip([chars])	|返回去掉左右char字符的字符串(默认char为空白字符)
S.lstrip([chars])	|返回去掉左侧char字符的字符串(默认char为空白字符)
S.rstrip([chars])	|返回去掉右侧char字符的字符串(默认char为空白字符)
S.upper()	|生成将英文转换为大写的字符串
S.lower()	|生成将英文转换为小写的字符串
S.replace(old, new[, count])	|将原字符串的old用new代替，生成一个新的字符串,可选字符串, 替换不超过 count 次
S.startswith(prefix[, start[, end]])	|返回S是否是以prefix开头，如果以prefix开头返回True,否则返回False,
S.endswith(suffix[, start[, end]])	|返回S是否是以suffix结尾，如果以suffix结尾返回True,否则返回False
S.title()	|生成每个英文单词的首字母大写字符串
S.isnumeric()	|判断字符串是否全为数字字符

# list方法
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

# dict方法
 方法 |	说明
 ---|---
D.clear()       |	清空字典
D.pop(key)      |	移除键，同时返回此键所对应的值
D.copy() 	    |返回字典D的副本,只复制一层(浅拷贝)
D.update(D2)    |	将字典 D2 合并到D中，如果键相同，则此键的值取D2的值作为新值
D.get(key, default=None) |	返回键key所对应的值,如果没有此键，则返回default
D.keys() 	    |   返回可迭代的 dict_keys 集合对象
D.values()      |	返回可迭代的 dict_values 值对象
D.items()       |	返回可迭代的 dict_items 对象

# tuple方法
方法|说明
---|---
count | 计数
index | 返回索引

# set 方法
方法 |	意义
---|---
S.add(e) 	|在集合中添加一个新的元素e；如果元素已经存在，则不添加
S.remove(e) 	|从集合中删除一个元素，如果元素不存在于集合中，则会产生一个KeyError错误
S.discard(e) |	从集合S中移除一个元素e,在元素e不存在时什么都不做;
S.clear() |	清空集合内的所有元素
S.copy() 	|将集合进行一次浅拷贝
S.pop() 	|从集合S中删除一个随机元素;如果此集合为空，则引发KeyError异常
S.update(s2) 	|等同于 S |= s2, 用 S与s2得到的全集更新变量S
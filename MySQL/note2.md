# 表结构操作(操作字段)
1. `alter table 表名 执行动作;`
2. 添加字段 (add)
    - alter table 表名 add 字段名 数据类型; 
    - 直接在最后一列的位置添加字段
        - alter table a1 add idcard int ;
    - 在第一行添加
        - alter table a1 add idcard int first;
    - 在name后面插入
        - alter table a1 add idcard int after name;
3. 删除字段
    - `alter table 表名 drop 字段名;`
4. 修改数据类型
    - `alter table 表名 modify 字段名 新数据类型;`
5. 表的重命名(rename)
    - `alter table 表名 rename  新表名;`
6. 表字段重命名(change)
    - alter table 表名 change 原名 新名 数据类型

## 表记录管理
1. 插入记录 `insert into 表名 values(),(),...;`
2. 查询记录 `select * from 表名 where 条件;`
3. 删除记录 `delete from 表名 where 条件;`
    - <font color=777FFF> 如果只写` delete from 表名 `表示清空所有记录</font>
4. 更新数据 `update 表名 set 字段1=值,字段2=值,...where 条件;`
    - 在做表更新时 <font color=777FFF> update 必须写where条件</font>

#  运算符
## 数值比较/字符比较
1. 数值比较: = != > >= < <=
2. 字符比较: = != 

## 逻辑运算符
1. 条件1 and 条件2;(查询同时满足两个条件的数据)
2. 条件1 or 条件2;
    - 查询满足条件一或者时满足条件2的数据
## 范围内比较
1. between 值1 and 值2 ;
    - 设置范围在 值1 和 值2 之间
2. where 字段名 in(值1, 值2, 值3,..);
    - 匹配字段值在in给出的范围内的数据
3. where 字段名 not in (值1, 值2, ...);
    - 匹配字段值不在指定范围内的数据
## 匹配空 where 字段 is null;
- 匹配非空 where 字段 is not null;
- is null  / is not null   
- 匹配"" (不管里面多少个空格) 可以直接用=""来匹配
## 模糊查询
1. 格式 :
    - where 字段名 like 表达式
2. 表达式:
    - _:表示匹配一个字符
    - %:表示匹配0到多个字符
3. 示例
    - 查找姓名包含两个字符以上的数据
    - select * from sanguo where name like"__%";
    - NULL不会被匹配出来, 空字符串会被正常匹配
4. 匹配姓赵的数据
    - where name like '赵%_';
    - 更改查询结果中的显示字段
    - select name as n from .....

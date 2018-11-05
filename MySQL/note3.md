# SQL 查询
## 完整的查询语句由一下关键字组成
- 顺序为书写顺序,序号是MySQL执行顺序
-    3 select-->   查找  
     1 where -->   条件  
     2 group by -->  分组  
     4 hacing -->  
     5 order by -->  排序  
     6 limit -->  分页  
## order by 对查询结果进行排序
- 格式: ...order by 字段名 ASC(升序)/DESC(降序)
- 示例
    - 讲英雄按照防御值从高到底排列
        - `select * from sanguo order by fangyu DESC;`
## limit 分页查询
- 永远放在SQL语句的最后书写
- 分页用来控制显示多少条结果中的数据
1. 语法
    1. limit n ; 表示显示n条数据
    2. limit m,n; 表示从第m+1条记录开始显示,显示n条
## select 查询
- select *
- select 字段
- select 聚合函数 where...
1. 聚合函数
    - 最大值 最小值 求和 平均值 计数
## 聚合函数
- avg(字段名)
- sum(字段名)
- max(字段名)
- min(字段名)
- count(字段名) : 统计该字段记录的个数
    - 统计中""会被统计但是NULL不会被统计
    - select count(id) as nub from sanguo where gongji > 200 and country = "蜀 国";
## group by 分组
- 计算每个国家的平均攻击力
- select countrt , avg(gongji) from sanguo group by country;
- 先分组再聚合
- 练习: 查找所有国家的男英雄中,英雄数量最多的前两名. 显示国家名称和英雄数量
    - `select country,count(name) from sanguo where sex = '男' group by country order by count(name) DESC limit 2;`
- 注意
    - 如果select 后字段和group by 后字段不一致,则select后字段必须聚合
## having 对分组后的数据进行二次筛选
- `select country,count(name) from sanguo where sex = '男' group by country order by count(name) DESC limit 2;`
- 通常与group by 配合使用, having就一定有group by
- having 语句的存在弥补可where关键字不能与聚合函数联和使用的不足,where 只能操作表中实际存在的字段

## distinct 不系那是字段的重复值

- select distinct 字段名,字段名2 from 表名 
    - 字段名和字段名2两个字段都相同才会去重
- distinct 不能对任何字段做聚合处理

## 在查询表记录时可以做数学运算
- 运算符 + - * / %
- 所有英雄攻击力翻倍
    - select gongji*2 from sanguo 

# 嵌套查询(子查询)
## 定义:
- 把内层的查询结果作为外层的查询条件
## 语法
- `select ... from 表名 where 字段名 运算符 (查询)`
- 找出小于平均值的
    - `select name,gongji from sanguo where gongji < (select avg(gongji) from sanguo)`
- 找出每个国家攻击力最高的英雄名字和攻击力
    - 有bug的`select name,gongji from sanguo where gongji in ( select max(gongji) from sanguo group by country);`
    - 正常的,再另外加个判断`select name,gongji from sanguo where (country,gongji) in ( select country,max(gongji) from sanguo group by country);`


# 多表查询

## 两种方式
1. 笛卡尔积(不加where条件)
    - select 字段1, 字段2 from 表1,表2;
2. 多表查询(加where条件)
    - select 字段1,字段2 from 表1,表2 where 条件;
        - `select sheng.s_name,city.c_name from sheng,city   where   sheng.s_id = city.cfather_id;`
        - `select sheng.s_name,city.c_name,xian.x_name from sheng , city, xian where sheng.s_id = city.cfather_id and city.c_id =  xian.xfather_id ;`                              


# 连接查询
- 内连接(和多表查询等价,只显示符合天剑的记录)
    - 语法格式
        - ` select 字段名 from 表1 inner join 表2 on 条件  inner join 表3 on 条件....;`
        - et显示省市县的信息`select sheng.s_name,city.c_name,xian.x_name from sheng inner join city on sheng.s_id = city.cfather_id inner join xian on city.c_id = xian.xfather_id;`
- 外链接
    1. 左连接
        - 定义: 以左表为主显示查询结果

    2. 右链接
        - 定义: 以右表为主显示查询结果

    - et显示市的全部信息 `select sheng.s_name,city.c_name,xian.x_name from sheng right join city on sheng.s_id = city.cfather_id left join xian on city.c_id = xian.xfather_id;`


# 约束

- 非空约束(not null)
- 默认约束(default 默认值)
    - `create table t3( id int(3) zerofill, usename varchar(20) not null, sex enum("M","F","S") not null default "S" );`

# 索引 (BTREE)
- 定义
    - 对数据库中表的一列或者多列的值进行排序的一种结构
- 优点
    - 加快数据的检索速度
- 缺点
    - 占用物理存储空间
    - 当你对表中的数据更新的时候,索引需要动态维护,占用了一定的系统资源,降低数据的维护速度
- 索引示例
    1. 开启运行时间检测
    - set profiling = 1
    2. 执行一条查询命令(没有创建索引)
    - select name from t1 where name ="lucy8888"
    3. 在name字段创建索引
    - create index name on t1(name);
    4. 再执行一条查询命令
    - select name from t1 where name ="lucy8888"
    5. 对比执行时间
    - show profiles;


# 索引的分类
1. 普通索引(index)&& 唯一索引(unique)
    - 使用规则
        - 都可以设置多个字段
        - index无约束,unique字段值不能重复,但可以为NULL,
        - 把经常用来查询的字段在设置为索引字段
        - index的KEY标志:MUL   unique: UNI
    - 创建表时创建索引
        - `create table 表名(..... .... index(name), index(id),unique(phnumber), unique(cardnumber));`
    - 已有表中创建
        - create [unique] index 索引名 on 表名(字段名);
    - 查看索引
        - desc 表名;  --> KEY标志
        - show index from 表名;
    - 删除索引
        - drop index 索引名 on 表名;
        
    - `select user_id,count(user_id) from comment group by user_id order by count(user_id)  DESC limit 10;`
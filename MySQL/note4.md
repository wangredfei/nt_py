

# 主键(primary key)  自增长属性(auto_increment)
- 使用规则
    1. 只能有1个主键字段
    2. 约束 : 不允许重复,且不能为NULL
    3. KEY标志 : PRI
    4. 通常设置记录编号的字段id,能唯一锁定1条记录
- 创建表时
    - `create table 表名(id int primary key auto_increment,...)auto_increment=10000,charset=utf8,engine=InnoDB;`
- 已有表
    - `alter table 表名 add primary key(id);`
- 删除
    1. 删除自增长属性(modify)
        - `alter table t1 modify id int;`
    2. 删除主键
        - `alter table t1 drop primary key;`

# 外键(foreign key)
- 定义 让当前表字段的值在另一个表的范围内选择
- 语法
    - foreign key(参考字段名)
    - reference 主表(被参考字段名)
    - on delete 级联动作
    - on update 级联动作
- 使用规则
    - 主表 从表字段数据类型要一致
    - 主表被参考字段: 主键
- 示例
    -`create table stab(stu_id int, name varchar(20),money smallint,foreign key(stu_id) references jftab(id) on delete cascade on update cascade);`
- 删除外键
    - alter table 表名 drop foreign key 外键名;
    - 外键名: show create table 表名;
- 已有表中添加
    - alter table 表名 add foreign key ......
- 级联操作
    - cascade 数据级联删除 更新(参考字段)
    - restrict(默认) 从表有相关联记录,不允许主表操作
    - set null 
        -  主表删除 更新,从表相关联记录字段值设置为NULL


# 锁
- 目的: 解决客户端并发访问的冲突问题
- 锁分类
    1. 锁类型
        1. 读锁( 共享锁 )
            - select : 加读锁以后别人不能更改表记录,但可以进行查询
        2. 写锁( 互斥锁 )
            - update : 加写锁后别人不能查也不能改

    2. 锁粒度
        1. 表级索: 一人进来锁整个表 = 加读锁 写锁

        2. 行级锁: 加读锁 写锁

# 存储引擎(处理表的处理器)
- 基本操作
    - 查看所有的存储引擎`show engines;`
    - 查看已有表的存储引擎`show create table 表名;`
    - 指定存储引擎`create table 表名(...)engine= MyISAM;`
    - 已有表 ` alter table 表名 engine=InnoDB`
- 常用的存储引擎的特点
    - InnoDB 
        1. 支持外键 事物 事务回滚
        2. 支持行级锁
        3. 共享表空间
            - 表名.frm: 表结构和索引文件
            - 表名.ibd: 表记录
    - MyISAM
        1. 支持表级锁
        2. 独享表空间
            - 表名.frm:表结构
            - 表名.MYD:表记录(my data)
            - 表名.MYI:索引文件(my index)
    - MEMORY
        - 表结构存储在硬盘中,表记录存储在内存中 ,服务/主机重启后,表结构还在,表记录消失
- 如何决定使用哪个存储引擎
    - 执行查询操作多的表 用MyISAM 如果使用InnoDB浪费资源
    - 执行写操作多的表   用InnoDB 

# 数据备份
1. 完全备份
2. 增量备份
- mysqldump,在linux终端中操作.
- 命令格式
    - ` mysqldump -uroot -ptarena 源库名 >路径/文件名.sql`
- 源库名表示方式
    - --all-databases 备份所有库
    - 库名             备份单个库
    - -B 库1 库2 库3   备份多个库
    - 库名 表1 表2 表3  备份制定库的多张表
- 数据恢复
    - 命令格式
        - `mysql -uroot -p 目标库名 < XXX.sql`
        - `mysql -uroot -p db4 < db4.sql`
    - 从所有库备份中恢复某一个库(--one-database)
        - `mysql -uroot -p --one-database 库名 < all.sql`
    - 示例
        1. 在MOSHOU.sheng新增一条记录
            - 1insert into sheng (s_id,s_name) values("30001","青海省")
    
    - 注意
        - 恢复库时,如果库不存在,则必须先创建空库
        - 恢复库时,恢复到原库会讲表中数据覆盖,新增表不会删除

# 数据导入
- 作用: 把文件系统的内容导入到数据库表中
- 语法格式
    ```
    load data infile "/var/lib/mysql-files.文件名"
     into table 表名
      fields terminated by "分隔符" 
      lines terminated by "\n" 
    ```
- 把scoreTable.csv文件导入到数据库表中
    - 在数据库创建对应的表
        ```
        create table scoretab(
        id int, name varchar(20),
        score float(5,2)
        ,phnum char(11),
        class char(7))
        charset = utf8;
        ```

    - 把文件拷贝到数据库的搜索路径中
        ```
        1. 查看搜索路径
        show variables like "score_file_priv";
        2. 复制
        sudo cp scoreTable.csv /var/lib/mysql-files/
        ```

    - 执行数据导入语句
        ```
        load data infile "/var/lib/mysql-files/scoreTable.csv" 
        into table scoretab
        fields terminated by "," 
        lines terminated by "\n";
        ```
# 数据导出
- 讲数据库中表的记录导出到系统文件里
- 语法格式
    ```
    select ... from 表名 where 条件   
    into outfile "/var/lib/mysql-files/文件名"   
    fields terminated by "分隔符"   
    lines terminated by "\n";`  
    ```
- et 
    - 把省表中所有记录导出来

# Mysq1 用户账户管理

1. 开启MySQL远程连接
    ```
    1. sudo -i 
    2. cd /etc/mysql/mysql.conf.d/
    3. sub1 mysqld.cnf
        - bind-adress = 127.0.0.1
    4. /etc/init.d/mysql restart
    ```
2. 添加授权用户 
    1. 用root用户登录mysql
    2. 授权
        - `mysql > grant 权限列表 on 库名.表名 to "用户名"@"%" identified by "密码" with grant option;`
        - 权限列表
            - `all privileges, select update 
        - 库.表
            - *.*  库名.*
    3. 示例
        - 添加用户tiger,密码123,对所有库的所有表有所有权限;
        - 添加用户rabbit,密码123,对db4有所有权限

# Homework
- 综述：两张表，一张顾客信息表customers，一张订单表orders 
1. 创建一张顾客信息表customers，字段要求如下：  
  c_id 类型为整型，设置为主键  
  c_name 字符类型，变长，宽度为20  
  c_age 微小整型，取值范围为0~255(无符号)  
  c_sex 枚举类型，要求只能在('M','F')中选择一个值  
  c_city 字符类型，变长，宽度为20  
  c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位  

  在表中任意插入3条记录,c_name为"Zhangsan","Lisi","Wangwu", c_city尽量	写  "Beijing","Shanghai" ......  
```
    insert into customers values  
    (1,"Zhangsan",25,"M","Beijing",8000),  
    (2,"Lisi",30,"F","Shanghai",10000),  
    (3,"Wangwu",27,"M","Shenzhen",3000);  
    create table customers(
    -> c_id int primary key,
    -> c_name varchar(20),
    -> c_age tinyint unsigned,
    -> c_sex enum("M","F"),
    -> c_city varchar(20),
    -> c_salary float(12,2),)
    -> ;create table passwd(name varchar(10),password varchar(10),uid int,gid int,ppdesc varchar(20),menu varchar(20),ccc varchar(15));

```
2. 创建一张订单表orders，字段要求如下：  
  o_id 整型  
  o_name 字符类型，变长，宽度为30  
  o_price 浮点类型，整数最大为10位，小数部分为2位  
  设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步  
  在表中任意插入5条记录(注意外键限制)  
  o_name分别为"iphone","ipad","iwatch","mate9","r11",其他信息自己定  
    insert into orders values  
    (1,"iphone",5288),  
    (1,"ipad",3299),  
    (3,"mate9",3688),  
    (2,"iwatch",2222),  
    (2,"r11",4400);  
```
 create table orders(o_id int,
    -> o_name varchar(30),
    -> o_price float(12,2),
    -> foreign key(c_id) references customers on delete cascade on delete cascade);
```
3. 返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录  
- `select * from customers where c_salary>4000 or c_age <29 limit 2;`
4. 把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
  update customers set salary=salary*1.15 ...
- `update customers set c_salary=c_salary*1.15 where c_age >=25 and (c_city='Shanghai' or c_city = 'Beijing');`
5. 把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录	
- `select * from customers where c_city="Beijing" order by c_salary DESC limit 1;`
6. 选择工资c_salary最少的顾客的信息
- `select * from customers order by c_salary ASC limit 1;`
7. 找到工资大于5000的顾客都买过哪些产品的记录明细
- `select * from orders where o_id in (select c_id from customers where c_salary > 5000);`
				
8. 删除外键限制
- `show create table orders ;`
- `alter table orders drop foreign key 外键名`
9. 删除customers主键限制
- `alter table customers drop primary key`
## 2. 把/etc/passwd文件导入到数据库表中,userinfo
  tarena  :  x   :  1000  :  1000
  用户名    密码    uid号    gid号
  :  tarena,,,  :  /home/tarena  :  /bin/bash
  用户描述         主目录           登录权限

  7列,6个:隔开



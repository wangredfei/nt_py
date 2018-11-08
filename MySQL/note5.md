# E-R 模型(Entry-Relationship)

## 定义
- 实体关系数据模型, 用于数据库的设计 (利用一张图反应项目里面数据关联)
## 实体
- 描述客观事物的概念(一个人 一本书 一个学生)
- 表示方法 : 矩形框
## 属性
- 实体具有的某种特性
- 表示方法:椭圆形
## 关系
- 实体之间的关系
1. 一对一(1:1) : 老公 对 老婆
    - A 中一个实体, B中只能有一个实体与其发生关联
    - B 中一个实体, A中只能有一个实体与其发生关联
2. 一对多(1:n) : 父亲 对 好多孩子
    - A 中一个实体, B中有多个实体与其发生关联
    - B 中一个实体, A中只能有一个实体与其发生关联

3. 多对多() : 兄弟姐妹 对 兄弟姐妹
    - A 中一个实体, B中有多个实体与其发生关联
    - B 中一个实体, A中有多个实体与其发生关联
## 数据库三范式
1. 第一范式(1NF) : 列不可拆分
2. 第二范式(2NF) : 唯一标识
3. 第三范式)3NF) : 引用主键
- 后一个范式,都是在前一个范式的基础上建立的

## 数据库关系的实现
- 1:1 : 主外键关联, 添加唯一约束
- 1:n : 主外键关联
- n:n : 利用中间表关联


# 事物和事物回滚

## 定义:
- 一件事从开始发生到结束的过程

## 作用
- 确保数据的一致性

## 操作事务
- 开始事物
    - begin

- 终止事物
    - commit
- 回滚
    - rollback

- 事物
    - 只针对于表记录操作(增删改)有效,对于库和表的操作无效


# MySQL 与Python交互 (pymysql模块(3) MySQLdb模块(2))

## 在线安装
- sudo pip3 install pymysql
- sudo pip install mysql-python
## 离线安装 
- 下载安装pymysql-0.9.1.tar.gz
## 环境准备 
1. 创建库 db5 , utf8
    - create database db5 charset utf8;
2. 创建表 t1
    - create table t1(id int primary key auto_increment, name varchar(20), score float(5,2));
3. 插入三条记录
    - insert into t1(name,score) values ("李白",60),("杜甫",75),("白居易",80);
## 使用教程
1. 数据库链接对象
    - pymysql.connect(...)
2. 游标对象 
    - cursor = db.cursorr()
3. 执行命令
    - cursor.rxrcute("sql命令")
4. 提交
    - db.commit()
5. 关闭游标
    - cursor.close()
6. 断开连接
    - db.close()

## pymysql.connect()参数
- host
- user
- password
- database
- charset
- port : 端口号(3306)

## 数据库链接对象(db)的方法
1. db.cursor() : 创建游标对象
2. db.commit() : 提交到数据执行
3. db.rollback() : 回滚
4. db.close()   : 断开与数据库链接

## 游标对象(cur)的方法
1. cur.execute(sql命令) : 执行sql命令
2. cur.close()  : 关闭游标对象
3. cur.fetchone() : 取一条(查询语句) 得到一个元组
4. cur.fetchmany(N) : 取N条     得到一个大元组,内含小元组
5. cur.fetchall() : 取所有      得到一个大元组,内含小元组


# MySQL调优
1. 选择合适的存储引擎
    1. 读操作多 : MyISAM
    2. 写操作多 : InnoDB
2. 创建索引
    在select where  order by常涉及到的字段建立索引
3. SQL语句优化(避免全表扫描)
    1. where子句中,不使用!=,否则放弃索引全表扫描
    2. 尽量避免NULL判断,否则...
      优化前 : select num from t1 where num is null;
      优化后
        在num字段上设置默认值0,确保num字段无空值
	select num from t1 where num=0;
    3. 尽量避免 or 连接条件,否则... ...
      优化前 : select id from t1 where id=10 or id=20
      优化后 :
        select id from t1 where id=10
	union all
	select id from t1 where id=20;
4. 模糊查询尽量避免使用前置%,否则...
      select name from t1 where name like "%c%";
5. 尽量避免使用 in 和 not in
      select id from t1 where id in(1,2,3,4);
      用 between 1 and 4 代替
6. 尽量避免使用 select * ... ,不要返回用不到的任何字段

5. WorkBench图形化界面管理工具
   Navicat


















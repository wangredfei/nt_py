# MySQl概述

## 1 什么是数据库
- 就是存储数据的仓库
- 电商公司,游戏公司,金融机构,政府部门....
## 2 提供数据库服务的软件
1. 软件分类
    - MySQL,Oracle,SQL-sever,DB2,MongoDB,MariaDB...
2. 生产环境中如何选择使用哪一种数据库软件
    1. 是否开源
        1. 开源软件:MySQL, MongoDB, MariaDB
        2. 商业软件:Oracle, DB2, SQL-Server
    2. 是否跨平台
        1. 不跨平台:SQL-Server
        2. 跨品台: ...
    3. 公司类型
        1. 用商业软件:政府机构,金融机构
        2. 用开源软件:游戏公司,电商公司,论坛,贴吧网站


## 3 MySQL 数据库有什么特点
1. 关系型数据库
    1. 关系型数据库的特点
        1. 数据以行和列(表格)形式存储
        2. 表中每一行叫一条记录,每一列叫一个字段
        3. 表与表之间的逻辑关联叫关系
    -  实例
        1. 关系型数据库存储数据
            ```
            表1 学生信息表
               姓名    年龄    班级
                安      20      3
                孔      18      1
            表2 班级信息表
                班级    班主任      
                三班    杨永胜
                四班    李金田
            ```
        -  非关系型数据库存数据
            ```
             {"姓名":"安", "年龄":"20", "班级":"三班", "班主任":"杨永胜"}
             {"姓名":"孔", "年龄":"18", "班级":"四班", "班主任":"李金田"}
            ```
    2. 跨平台
        - 可以再Windows, Linux, Unix上运行
    3. 支持多种编程语言
        - python, Java, PHP...

## 4 数据库软件, 数据库, 数据仓库的概念
1. 数据库(DateBase简写DB)
    - 储存在计算机内的有组织, 可共享的数据集合
2. 数据库软件(数据库管理系统)
    - 一个软件, 看得见, 可操作的工具, 可以通过SQL语句来操作数据库(SQL: 结构化查询语句)
3. 数据仓库(Data WareHouse 简写,DW,DWH)
    - 数据量要比数据库大的多,主要用于数据分析和数据挖掘
    - et:
        数据库:购物车表,用户信息表
        数据仓库: 分析哪个时间段用户的访问量最大,哪个用户一年中购物最多...


# MySQL安装
1. Ubuntu安装MySQl服务
    1. 安装服务端
        - ` sudo apt-get install mysql-server`
    2. 安装客户端
        - ` sudo apt-get install mysql-slient`
    3. Ubuntu 安装软件
        - ` sudo apt-get update `
            - 访问源列表中的每个网址,读取软件列表,保存到本地/var/lib/apt/lists
        - ` sudo apt-get upgrade`
            - 把本地已安装软件与刚下载的软件列表进行比对,如果发现已安装软件的版本低,则更新软件
        - ` sudo apt-get -f install`
            - 修复依赖关系
    - [卸载重装](https://www.cnblogs.com/xusir/p/3342722.html)
2. Windows 安装MySQL
    1. 下载安装包
        - mysql-installer***5.7.24.msi
    2. 流程安装
3. Mac 电脑安装MySQL
    1. 下载安装包(dmg --> pkg)
    2. 设置环境变量
        1. vi .base_profile
        2. 在末尾写如下内容,保存并退出
            - `export PATH=${PATH}:/usr/local/mysql/bin`
            - `PATH="${PATH}":/usr/local/mysql/bin`
    3. 在命令行下 
        - `$ source .base_profile`
    4. 登录测试 
        - `mysql -uroot -p`


# 启动和链接数据库       
1. 启动服务端(终端下启动)
    1. 查看当前MySQL状态是否可用
        - `sudo /etc/init.d/mysql status`
    2. 启动MySQL服务
        - `sudo /etc/init.d/mysql start | stop | restart` 
2. 客户端链接
    1. 命令格式:
        - `mysql -h主机地址 -u用户名 -p密码`
        - et:
            - `mysql -hlocalhost -uroot -p123456`
    2. 本地连接可以省略-h选项

# 基本SQL命令
## 1. SQL命令的使用规则
1. SQL命令不区分大小写
2. 区分中英文的标点符号,一律使用英文标点符号
3. 每条命令以;号结尾
4. 使用\c终止当前命令的执行
## 2. 库的管理
1. 库的基本操作
    1. 查看已有的库
        - `show databases;`
    2. 创建库
        - `create database 库名;`
        - 创建的同时制定字符集
        - `create database 库名 character set utf8;`
    3. 查看创建库的语句(字符集)
        - `show create database 库名;`
    4. 查看当前所在库
        - `select database();`
    5. 切换/选择库
        - `use 库名;`
    6. 查看当前库中所有的表
        - `show tables;`
    7. 删除库
        - `drop database 库名;`
2. 库名的命名规则
    1. 库名由数字,字母,下划线组成,不能使用纯数字
    2. 库名区分大小写(命令不区分大小写)
        - et:
            1. SQL命令不区分大小写
                - `CREATE DATABASE TESTDB`
                - 等价与       
                - `create database TESTDB`
            2. 库名区分大小写
                - `create database TESTDB`
                - `create database tesedb`
                - 创建了两个库
    3. 不能使用特殊字符和MySQL的关键字

## 3. 表记录管理
1. 表的管理
    1. 表的基本操作
        1. 创建表
            - `create table 表名(字段名 数据类型, 字段2 数据类型 ,...);`
            - 创建的同时指定字符集
            - `create table 表名(字段1 数据类型, 字段2 数据类型,.....)character set utf8;`
        2. 查看已有表的字符集
            - `show create table 表名;`
        3. 查看表结构
            - `desc 表名;`
        4. 删除表
            - `drop table 表名;`
    - 注意 : 
        1. 如果涉及到多个库切换操作表,一定不要忘了切换数据库
        2. 所有的数据在数据库中都是以文件的形式存储的,存放目录为
2. 表记录管理(操作数据)
    1. 插入数据(insert)
        - `insert into 表名 values(值1),(值2),....;`
        - 例如: ` insert into stuinfo values(1,'安',300),(2,'孔',80);`
        - 括号总的值实际代表的时一行,一条记录
    2. `insert into 表名(字段1,字段2,..) valuse(值1),(值2),...;`
        - et:
            - `insert into stuinfo(name,age) value('小邵',20),("小宋",20);`
    3. 查询数据(select)
        1. select * from 表名; //查询表中所有数据
        2. select * from 表名 where 条件;//查询表中满足条件的数据
        3. select 字段1,字段2 from 表名 [where 条件] // 查询指定字段的数据

3. 更改默认字符集
    1. 方法:修改MySQL的配置文件
    2. 步骤 
        1. 获取root权限
            - sudo -i
        2. cd /etc/mysql/mysql.conf.d/
        3. 备份(相当重要) 
            cp mysqld.cnf mysqld.cnf.bak
        4. 修改
            - subl[/vi] mysqld.cnf
            - 找到 [mysqld]
            - 添加 character_set_server = utf8 
        5. 重启
            - sudo /etc/init.d/mysql restart
        6. 连接客户端
## 4. 数据类型
1. 数字类型
    1. 整形 
        - int 大整形(4个字节)
            - 取值范围0~2**32-1
        - tinyint 微小整形(1一个字节)
            - 有符号整形(默认)
                - id tinyint signed
            - 无符号整形(unsigned)
                - 取值范围 0~255
                - age tinyint 
        - smallint 小整形(2字节)
        - bigint 极大整形(8个字节)
    2. 浮点型
        - float (四个字节, 最多显示7个有效位)
            1. 用法
                - 字段名 float(m,n)
                - m表示总位数,n表示小位数的位数
                - et:
                   -  score float(3,1)
        - double (8个字节)
            - float是单精度 误差大
            - double 是双精度,误差稍小,在mysql内部运算时,都采用double运算
        - decimal (最多可显示28个有效位)
            - 用法同float
    3. 数值类型占用的存储空间
        - 整数和小数分开存储的,需要各自计算所需的字节数
        - 规则
            - 将9的倍数包装成4个字节
        - 余数占用字节对照表
            - 余数  | 字节
            ---|---
            0|0
            1-2|1
            3-4|2
            5-6|3
            7-8|4

2. 字符类型
    1. char(size) 1< size < 255
        - 特点:定长存储
        - 固定分配10个字符的空间存储数据
    2. varchar(size) 1 < size < 65535
        - 特点:变长存储
        - 根据数据的实际长度分配空间,小于10个字符按实际的字符数分配空间,最大可分配10个字符的空间,超过十个字符的数据,无法存储,会报错
    - 注意:
        1. 定长和变长字符类型在存储空间上区别较大
            - char定长存储,优点快,缺点浪费存储空间但是性能高
            - verchar 变长存储,节省空间,但是性能低
        2. 字符类型的显示宽度与数值类型宽度的区别
            - 数值类型的宽度为显示宽度,用于select查询是显示结果,和占用存储空间无关即时超出显示宽度,只要没有超出数据类型的取值范围都可以插入成功
            - 字符类型的宽度不仅是显示宽度,还是最大字符数,超出就无法存储
            - 数值类型如果指定显示宽度,而数据长度小于宽度,会自动补0,补充显示宽度
                - 结合zerofill 属性查看效果
                    - id int(5) zerofill
    3. text/longtext(4G)/blob/longblob(4G)
        - test 相关的类型可用来存储大批量的文本数据(博文等)
        - blob 相关的类型更适合与二进制数据的存储(图片)
3. 枚举和集合

4. 日期和时间类型

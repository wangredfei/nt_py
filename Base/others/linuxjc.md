#老师邮箱：
    wangweichao@tedu.cn
    weimz@tudo.cn
    fenghua@tedu.cn
    fhua1995


#linux操作系统

##教学环境安装：
- 虚拟机工具：
    VMwareWorkstation
- 　下载linux纯净版镜像文件　．ios文件格式
- 新建虚拟机　
- ＣＤ／ＤＶＤ　插入光盘，或者使用下载好的ｉｓｏ镜像文件
- 开启虚拟机＝　通电开机
- 安装完成后，再安装一系列软件＼模块

#常用命令
##终端：ｃｔｒｌ＋ＡＬＴ＋Ｔ
- 用来输入命令
- 搜索计算机　gnome-terminal
##目录树
- 根：/   #所有文件的起始位置 
- 用户主目录：～
- 文件夹　－－　目录
##Linux命令基本格式
- 命令名　［选项参数］　［参数］　＃［］代表里面的内容可有可无

## pwd 获取当前所在位置

##　ls 查看当前目录下有哪些文件或文件夹
- 选项: -a -l
- 格式：
    - ls -l （列表显示）
    - ls -a (显示隐藏文件) # 一般以．开头的文件是隐藏文件
    - 或者　ls -al 
        - ls -la
        - ll

## 路径　
- 绝对路径
    - 从/目录开始的路径
- 相对路径
        不以/开头的路径
    　　
    - . 代表当前目录
    - ．．代表上一级目录
    - ～　用户主目录/家目录　

## 用户主目录/家目录
- 超级用户　:root
- 　创建用户时会自动在/home下创建一个和用户名同名的用户主目录
- 用户名：　tarena 主目录　：/home/tarena
- 用户名：　＃＃＃＃　主目录: /home/####

##  cd 切换目录（路径）
- cd              路径（可以是绝对路径或者是相对路径）
- cd /home/tarena
- cd ..           切换到上一级
- cd ../../..     切换到上一级的上一级的上一级
- cd / 　　　　　　　　　　　切换到根目录
- cd 　　　　　　　　　　　　　直接跳到用户主目录／或 cd ~
- cd - 　　　　　　　　　　　返回上一次操作目录

## tab 自动补齐(熟悉使用！！！！)
- 速度快
- 不容易错
- ｔａｂ不出来，说明要不多选，要不没有本文件
        摁两下

## mkdir 创建一个或者多个目录
- 格式: mkdir　［选项］ 目录名１　目录名２　．．
- 选项：　-p　逐级创建
- rmdir 删除
    - 逐级全部删除 -p
    - 如果不用 -p 则必须目录为空   

## touch 
- 作用：创建文件　
- ＃　若文件不存在则更新文件的修改时间

## 技巧类
- 自动补齐：ＴＡＢ键
- 翻出执行过的命令　：上下键　
    history　！　行数
- 清屏幕　
    CTRL+L
    输入　Clear
- 终止命令执行
    CTRL+C
- 终端字体
    增大：CTRL+shift+ '+'
    缩小：CTRL+"-"

## rm 删除文件　目录
- 选项：　
    - -r 删除全部目录
    - -f 强制删除 
    - -i 删除前给提示
- 常用　rm　-rf 文件／文件夹


## 通配符
- *　　：代表一个或者多个
- ？ 　：代表一个

## vi/vim 文本编辑器
- 三种模式：
    - 浏览模式＼插入模式＼命令行模式


- 进入插入模式
    - a 往后插入
    - i　往前插入
    - o　下一行插入
- 退出插入模式
   -  ＥＳＣ
- 命令行模式：
    - shift +: 然后输入wq
    - (:w 保存  :q 退出)
- 写入步骤
    - vi 文件名
    - 按　a/i/o  编辑文本
    - 按ＥＳＣ
    - 按shift+: 命令行模式
    - wq 　保存退出
    - q！不保存直接退出
    - w 　保存

> code.tarena.com.cn   
    - tarenacode  
    - code_2013

# linux 一点命令

## cp  复制
- cp [源文件]　路径
- cp -r [源目录]　路径
- cp *.txt 路径　
    - 代表复制以txt　结尾的
- 复制文件中改名
- cp -r［源文件］路径　／新的名称

## mv 　剪切
- 两个作用：
    - 剪切　重命名
- 剪切：
    - mv 文件名/目录　路径(可加/修改名称)
- 重命名：
    - mv 原文件名称　新名称（在当前路径下重新命名）

## cat 
- 将文件打印到终端

## tar 压缩与解压缩
- 格式
    - tar -zcvf 压缩包名字.tar.gz（一般以　.tar.gz结尾）　需要压缩的文件／目录

- **如果想在压缩的过程中把压缩包放在其他目录，则在压缩包名称前加位置**  
    - **例如：**  
        - **tar -zcvf ~/AID/压缩包名字.tar.gz（一般以　.tar.gz结尾）　需要压缩的文件／目录**

- 解压缩
    - tar -zxvf 压缩包名字.tar.gz [-c 路径]
    - -C :指定解压路径，不写默认解压到当前目录
- 选项含义

    - -z:压缩格式 用gzip对压缩包进行压缩
    - -c:创建包(create)
    - -v:显示压缩明细（verbose）
    - -f:file
    

## 文件权限
- 查看文件　ls -l  或ll

    - -rw-rw-r-- tarena tarena 2 bb.txt
- 最左一列　　－ 代表类型
    - d 目录
    - －　文件
    - l 链接
- 权限
    - r 读
    - w 写
    - x 可执行
- 分组：
    - 第一组：文件所有者权限 user 
    - 第二组：同组用户 group
    - 第三组：其他组用户 others
- 方式１
    - chmod 修改文件权限
        - 给所有用户添加相关权限
            - chmod(a)+x/-w A.txt
            - 代表　all

        - 给指定组用户修改权限

            - user:chmod u+x A.txt
            - group:chmod g+x A.txt
            - other:chmod o+x A.txt
-  方式２（通过数字方式修改）
    - chmod 644 A.txt  #rw-r--r--
    - r = 4
    - w = 2
    - x = 1
    - chmod 777 A.txt # rwxrwxrwx


**在一个目录下，不能同名，如果已经存在，然后touch则更新时间**

---

高阶一点的

---

## sudo:　　　　获取ｒｏｏｔ用户的权限执行ｌｉｎｕｘ命令
- sudo +命令＼
- 权限不够加ｓｕｄｏ

## df -h : 　
- 查看磁盘使用情况

## top:
- 任务管理器

## ps -aux | grep "想输出的结果"　例：firefox
- 查看某个应用程序的ｐｉｄ号



## kill -9 PID号 　：强制结束
- 杀死进程
- 需要先查看ＰＩＤ号


## ifconfig 
- 查看网络地址

## 管道　　
- 例子：
    - cat hello.py |grep "hello"
    - 输出：在终端输出含有hello行内容

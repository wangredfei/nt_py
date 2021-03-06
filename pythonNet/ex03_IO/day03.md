# IO (input  output)
- 在内存中存在数据交互的操作认为是IO操作
- 和终端交互 : Input print
- 和磁盘交互 : read write
- 和网络交互 : recv send
## IO密集型程序
- 在程序执行中有大量IO操作,而较少的cpu运算. 
- 特点 : 消耗CPU少.效率低,耗时长
## 计算密集型程序
- 在程序运行中,IO操作较少,cpu计算较多
- 特点,cpu消耗大,运算速度快

## IO 模型
- 阻塞IO
- 非阻塞IO
- IO多路复用
- 事件IO
- 异步IO
- ...

### 阻塞IO
- 阻塞IO是IO的默认形态
- 效率很低

- 阻塞情况
    - 因为某种条件没有达成造成的函数阻塞
        - accept  input  recv
    - 处理IO的事件较长产生的阻塞行为
        - 网络延迟,大文件的读写 

### 非阻塞IO
- 将原本阻塞的函数通过属性的设置改变阻塞行为,变为非阻塞

- sockfd.setblocking(bool)
    - 功能 : 设置套接字为非阻塞IO
    - 参数 : 默认True 表示套接字调用阻塞函数时为阻塞状态, 设置为False

- 超时检测,即设置一个最长的阻塞等待事件,超过后即不在阻塞
- sockfd.settimeout(sec)
    - 功能 : 设置套接字超时事件
    - 参数 : 设置的事件,秒
    * 超时检测不能和非阻塞通用,否则超时没有意义

### IO多路复用
- 定义 
    - 同时监控多个IO事件,选择其中能够执行的IO进行IO事件处理,  
        以此形成可以用时操作多个IO的行为模式,  
        避免一个IO阻塞造成其他IO均无法执行的情况.
- IO事件就绪: IO已经发生,内核需要交给应用程序处理

- 具体方法: select poll epoll
    - import select 

- select : windows linux unix
- poll : linux unix
- epoll : linux

### select 方法
- rs,ws,xs = select(rlist,wlist,xlist[,timeout])
- 功能: 监控IO事件,阻塞等待IO事件发生
- 参数:
    - rlist 列表 : 存放需要等待条件发生的IO事件
    - wlist 列表 : 存放需要主动处理的IO事件
    - xlist 列表 : 当发生异常需要处理的IO事件
    - timeout 超时时间
- 返回值:
    - rs 列表:rlist中准备就绪的IO 
    - ws 列表:wlist中准备就绪的IO
    - xs 列表:xlist中准备就绪的IO

- 注意: 
    1. IO多路富哦用占用计算机资源较少,效率较高
    2. wlist中如果有IO则select立即返回处理
    3. 在IO处理过程中不要出现死循环,影响IO监控

# 位运算
- `& ` 按位与
- `| ` 按位或
- `^ ` 按位异或
- `<<` 左移 : 右侧加0
- `>>` 右移 : 去掉低位
# poll 方法
## 创建
```
p = select.poll()
```
- 创建poll对象
- 返回值 : poll对象
## 注册
```
p.register(fd,event)
```
- 功能: 注册要关注的IO
- 参数: 
    - fd要关注的IO对象 
    - event 要关注的事件
- 常用事件类型 
    - POLLIN 读IO rlist
    - POLLOUT 写IO wlist
    - POLLERR 出错 IO xlist
    - POLLHUP 断开链接事件
- 例子: ` p.register(sockfd,POLLIN|POLLERR)`

## 取消关注的IO
```
p.unregister
```
- 功能: 取消关注的IO
- 参数: IO对象或者文件描述符

## 监控
```
events = p.poll()
```
- 功能: 阻塞监控IO事件发生
- 返回值: event 是一个列表
    - [(fileno,event),()...]
    - 每个就绪IO对应一个元组,元组中为该IO的fileno和就绪事件
- 返回值中没有IO对象,所以通过fileno配合IO对象字典查找

- sockfd.fileno()  获取套接字对应的文件描述符
- 文件描述符 : 系统中每一个IO操作系统都会分配一个整数作为编号，该整数即为这个IO操作的文件描述符。

## poll_server 步骤
1. 创建套接字
2. 设置套接字为关注
3. 建立fileno查找字典
4. 循环监控IO

# epoll 方法
## 使用方法: 
- 基本同poll对象相同
- 将生成对象函数改为 epoll
- 将所有关注IO事件类型改为EPOLL

## epoll 特点
- 是linux的专属多路复用方法
- 效率相比前两个高
- epoll可以监控更多的IO (select最多监控1024)
- epoll 支持更多的触发事件类型(EPOLLET边缘触发)


# 结构化数据
- `import struct`
- 原理: 将部分数据类型放在一起,转换成bytes格式数据包,并且可以按照指定格式解析bytes数据包
- ` struct.struct(fmt)`
- 功能: 生成struct格式包对象
- 常用fmt int ---  i /bytes ---  ns/float ---  f

##  打包
- 格式 : `st.pack(v1,v2,v3) `
- 功能: 要打包的数据
- 返回值 : 打包后的bytes

## 解包
- 格式: `st.unpack(bytes)`
- 功能: 将bytes格式数据包解析
- 参数: 要解析的数据包
- 返回值:数据元组

## pack()和unpack()可以通过struct模块直接调用
- 例子

# 本地套接字
- 功能: 本地两个程序之间利用套接字进行通信的一种方法

## cookie:

### linux文件类型 
- b(块设备文件)
- c(字符设备文件)
- d(目录)
- `-`(普通文件)
- l(连接文件)
- s(套接字文件)
- p(管道文件)

## 流程
1. 创建本地套接字
    - `sockfd = socket(AF_UNIX,SOCK_STREAM)`

2. 绑定本地套接字文件
    - `sockfd.bind(path)`

3. 监听
    - `sockfd.listen()`

4. 连接
    - `sockfd.accept()`
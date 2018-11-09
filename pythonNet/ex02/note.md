
# tcp套接字传输特征
1. 当一端退出时如果另一端阻塞在recv，此时recv会立    即结束阻塞返回空字串
2. 如果另一端不存在则在调用send发送时会出现
   Broken Pipe异常
3. 一个监听套接字可以同时连接多个客户端，也可以重    复使用


# 网络收发缓冲区
1. 减少和磁盘的交互
2. 协调收发速度（数据处理速度）

* send和recv实际是向缓冲区发送，从缓冲区接收

# TCP粘包

## 产生原因 ： 
1. tcp以字节流的方式进行数据传输，消息之间没边界
2. 多次发送的消息被一次接收

- 影响 ： 如果每次发送的内容是一个独立含义的个体此时         粘包会产生影响

## 处理粘包： 
1. 将消息结构化
2. 在消息结尾添加结束标志
3. 控制消息发送速度

# 基于UDP套接字的服务端

1. 创建数据报套接字
```
   sockfd = socket(AF_INET,SOCK_DGRAM)
```
2. 绑定地址
```
   sockfd.bind(addr)
```
3. 消息收发  
```
   data,addr = sockfd.recvfrom(buffersize)  
```
- 功能：接收UDP消息  
- 参数：每次最多接收多少字节消息  
- 返回值：data  收到的消息  
addr  消息发送方的地址  
```  
   n = sockfd.sendto(data,addr)  
```
- 功能 ： 发送udp消息  
- 参数 ： data 要发送的消息  bytes格式  
           addr  目标地址  
- 返回 ： 发送的字节数  

4. 关闭套接字
   sockfd.close()


# udp客户端

1. 创建数据报套接字
2. 消息发收
3. 关闭套接字

# cookie

- 获取命令行参数
```
import  sys
sys.argv  属性获取命令行内容
```
* 将命令行参数以字符串形式收集为一个列表

# tcp套接字和udp的区别
1. 流式套接字是以字节流方式传输数据，数据报则以数    据报形式传输
2. tcp传输会有粘包，udp不会
3. tcp保证传输的可靠性，udp不保证
4. tcp需要listen accept操作，udp不需要
5. tcp使用send  recv收发消息，udp使用
   sendto recvfrom

# 补充函数：
- sendall(data)
- 功能 参数 同send
- 返回值 ： 发送成功 None 失败得到异常


# 套接字属性

- sockfd.type    套接字类型
- sockfd.family  套接字地质族类型

- sockfd.getsockname()  获取套接字绑定地址

- sockfd.fileno()  获取套接字对应的文件描述符

- 文件描述符 : 系统中每一个IO操作系统都会分配一个整数作为编号，该整数即为这个IO操作的文件描述符。

* 文件描述符示系统识别IO的标志

- sockfd.getpeername()  获取连接端的地址信息

- sockfd.setsockopt(level,option,value)
    - 功能： 设置套接字选项，丰富或者修改套接字属性功能
    - 参数： 
        - level  要设置的套接字选项类别  SOL_SOCKET 
        - option  选择每个类别中具体的选项
        - value   要设置的值

    - 创建套接字后立即设置 

- sockfd.getsockopt(level,option)
    - 功能： 获取套接字选项值
    - 参数： level   选项类别  
        - option  每个选项类别对应的子选项
    - 返回值 ： 获取到的选项值
    

# udp应用之广播

- 广播 ： 一点发送，多点接收
- 广播地址： 每个网段的最大地址为广播地址

- 设置可以发送接收广播
```
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
```




# TCP应用之http传输

- http协议  超文本传输协议  应用层协议

- 用途 ： 网页的获取    数据的传输

- 特点 ： 
    1. 应用层协议，传输层选择tcp传输
    2. 简单，灵活，很多语言都有http专门接口
    3. 无状态协议，协议本身不要求记录传输的数据
    4. http1.1  支持持久连接

- 网页  请求过程：
    1. 客户端（浏览器）通过tcp传输 发送http请求给服务端
    2. 服务端接收到http请求后进行解析
    3. 服务端处理具体请求内容，组织响应内容
    4. 将响应内容以http响应格式回发给浏览器
    5. 浏览器接收响应内容解析展示

#  http请求  request 

## 请求格式

- 请求行 ： 具体的请求类别和请求路径
    - 格式 ：  GET  -----/----HTTP/1.1
        - 请求类别 ---- 请求内容 ---协议版本
    
    - 请求类别  每种类别代表要做不同事情
    - GET    获取网络资源
    - POST   提交一定的信息，得到反馈
    - HEAD   只获取响应头
    - PUT    更新服务器资源
    - DELETE   删除服务器资源
    - CONNECT  
    - TRACE   测试
    - OPTIONS  获取服务器性能信息

        
- 请求头 ： 对请求内容的基本描述

    - Accept-Encoding: gzip, deflate, br
    - Accept-Language: zh-CN,zh;q=0.9
    - Cache-Control: max-age=0
    - Connection: keep-alive

- （空行）

- 请求体: 请求参数或者提交内容

# HTTP 响应 (response)

## 格式

- 响应行 : 反馈响应的基本情况
    - 格式 : HTTP/1.1 | 200  | ok
        - 协议版本    |响应码  | 附加信息
    - 响应吗:
        - 1xx : 提示信息,请求被接收  
        - 2xx : 响应成功
        - 3xx : 响应需要进一步操作,重定向
        - 4xx : 客户端错误
        - 5xx : 服务器错误
        - 
- 响应头 : 
- 空行 
- 响应体: 回复给客户端的具体内容

- 要求
    1. 知道http协议的作用
    2. 了解网页访问的基本流程
    3. 掌握http协议 请求和响应的格式
    4. 知道http请求的基本类型,和响应码的含义


- 作业 ： 使用tcp完成一个文件的传输，要求可以传输文本文件也可以传输图片
        从客户端发给服务端，或者从服务端发给客户端均可



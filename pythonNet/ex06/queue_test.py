from multiprocessing import Queue
from time import sleep

# 创建消息队列
q = Queue(3)

q.put(1)
sleep(0.05)
print(q.empty())
#返回Ｔｒｕｅ,因为存入速度慢,　如果加延时,则会返回Flase0

q.put(2)
q.put(3)
print(q.full())
# q.put(4)# 满了会阻塞
# q.put(4,False)# 非阻塞满了会报错
# q.put(4,timeout=3) # 设置超时时间
print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())# 超出会阻塞
print(q.qsize())

q.close()
from multiprocessing import Pool
from time import ctime ,sleep

def worker(msg):
    sleep(2)
    print(msg)
    return msg
# 创建进程池对象
poll = Pool(processes = 4)
result = []
# 像进程池添加事件
for i in range(10):
    msg = 'apple%d'%i
    # r = poll.apply_async(func=worker, args=(msg,))
    poll.apply(func=worker, args=(msg,))
    # result.append(r)
# 关闭进程池
poll.close()
# 回收进程池
poll.join()
print("===============")

# for i in result:
    # print(i.get())
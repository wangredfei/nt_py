from multiprocessing import Process,Array
import time 

# # 开辟一个共享内存,存入整数列表
# shm = Array('i', [1,2,3,4,5])

# def fun():
#     for s in shm:
#         print(s)
#     shm[0]=1000
# p = Process(target = fun)
# p.start()
# p.join()
# for i in shm:
#     print(i)

shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
    shm[0] = b'H'

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i,end="")
print()
print(shm.value)# 打印字符串
# 1. 写一个程序，以电子时钟的格式打印时间：
#   　　格式:
#        HH:MM:SS
#       要求:每一秒钟变化一次　
def clock():
    import time
    while 1:
        now_t = time.localtime()
        h = now_t[3]
        m = now_t[4]
        s = now_t[5]
        print("{:0>2}:{:0>2}:{:0>2}".format(h,m,s),end = "\r")
        time.sleep(1)
    
clock()

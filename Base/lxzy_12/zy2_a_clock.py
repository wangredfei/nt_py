#   2. 编写一个闹钟程序，启动时设置定时时间，到时间后
#     打印一句，时间到，然后退出程序
def a_clock(t):
    
    import time
    while 1:
        now_t = time.localtime()
        h = now_t[3]
        m = now_t[4]
        s = now_t[5]
        print("{:0>2}:{:0>2}:{:0>2}".format(h,m,s),end='\r')
        if t[0] == h and t[1] == m and t[2] == s:
            print()
            print("时间到")
            return     
        time.sleep(1)
my_alarm = [17,42,50]
a_clock(my_alarm)
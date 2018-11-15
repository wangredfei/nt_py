import os
import time
# 会复制原有进程的所有运行空间,创建一个新的进程,并且会执行
a = 0
pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("New process")

    print(a)
    a = 10000
else:
    time.sleep(1)
    print("Old process")
    print('old',a)
print("=====The end====")
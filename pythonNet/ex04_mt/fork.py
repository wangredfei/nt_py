import os

# 会复制原有进程的所有运行空间,创建一个新的进程,并且会执行
pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("New process")
else:
    print("Old process")

print("=====The end====")
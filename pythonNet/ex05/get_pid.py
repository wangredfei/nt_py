import os

pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    print("Child PID", os.getpid())
    print("Get F ID",os.getppid())
else:
    print("Get child pid: ",pid)
    print(os.getpid())


    
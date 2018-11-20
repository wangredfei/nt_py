import sys
from select import select
from socket import *

s= socket()
s.bind(("0.0.0.0",8888))
s.listen(3)

# 监控IO
print("wait my IO")
rs, ws, xs = select([s,sys.stdin],[],[s],3)
print(rs,"\n",ws,"\n",xs)
print("ohh")


# 1.在终端输出菱形

for i in range(1,4):

    for j in range(3-i):
        print(" ",end='')
    for k in range(i*2-1):
        
        print('*',end='')
    print()
# print()
for l in range(0,2):
   
    for s in range(l+1):
        print(" ",end='')
    
    for c in range(3-l*2):
        
        print('*',end='')
    print()
print()

# ---------------------

#　2

a = 216//16
b = 216%16
print('在现代是%d斤%d两'%(a,b))

# ---------------------
# 3
hs = 100
ss = 5.0/9.0*(hs-32)
ks = ss+273.15
print("１００华氏温度转为摄氏温度是%.2f,转为开氏温度为%.2f"%(ss,ks))


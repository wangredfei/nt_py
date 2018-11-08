# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        zw = '%d * %d = %d' % (j ,i , i*j)  
     
        print("%-10s" % zw ,end="  ")
    print()
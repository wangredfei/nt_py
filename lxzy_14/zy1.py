#   1. 一个球从100米高空下落,每次落地后反弹高度为原高度
#     的一半,再落下,写程序:
#       1) 算出皮球在第10次落后反弹多高
#       2) 算出皮球在第10次反弹后经过多少米路程

height = 100 
km = 100
for i in range(10):
    height /= 2
    km += height*2
print(height)
print(km)
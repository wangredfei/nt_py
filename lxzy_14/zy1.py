#   1. 一个球从100米高空下落,每次落地后反弹高度为原高度
#     的一半,再落下,写程序:
#       1) 算出皮球在第10次落后反弹多高
#       2) 算出皮球在第10次反弹后经过多少米路程


def get_height(height,times):
    km = height
    for i in range(times):
        height /= 2
        km += height*2
    return height,km
print('返回的高度是%f,经过了%d米'% get_height(100,10))
# 1. 已经有列表：L = [3, 5]  
# 用索引颗切片操作，将原来列表改变为：  
# L = [1, 2, 3, 4, 5, 6]  
l = [3,5]
l[2:] = [6]
l[0:0] = [1,2]
l[3:3] = [4]
print("l = ",l)
# 将列表翻转：  
# L = [6, 5, 4, 3, 2, 1]  
l = l[::-1]
print("l = ",l)
# 然后删除最后一个元素  
# L = [6, 5, 4, 3, 2] 
del l[-1]
print("l = ",l)
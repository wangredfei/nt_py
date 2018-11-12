import copy
l = [1,2,3]
l1 = [l, 4, 5, 6]
l2 = l1 
l3 = l1.copy()
l4 = copy.deepcopy(l1)
# print(l1)
# print(id(l1))
# print(l2)
# print(id(l2))
# print(l3)
# print(id(l3))
# print(l4)
# print(id(l4))
# -----
# l1.append(8)
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# ------
l [2] = 33
print(l1)
print(l2)
print(l3)
print(l4)
# l4 始终都没有改变
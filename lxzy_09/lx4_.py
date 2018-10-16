def A(l):
    l = [4,5,6]
    print(l)

l = [1,2,3,4]
A(l)
print(l)
# 不可变
def A(l):
    l.append("ABC")
    print(l)

l = [1,2,3,4]
A(l)
print(l)

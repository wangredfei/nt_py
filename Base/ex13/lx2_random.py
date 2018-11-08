# l = list(range(10))
# random.sample(l,6)
# 生成重复的密码
def get_passward ():
    import random
    l = []
    for i in range(6):
        l.append(str(random.randint(0,9)))
    L = "".join(l)
    return L
print(get_passward())




def read_info(filename):
    '''此函数返回[{'name':"小张","age":20,"score":100},...]'''
    l = []# 此列表用于存储字典
    try :
        file = open(filename)
        while 1 :
            s = file.readline()
            if not s:
                break
            s = s.strip()
            ls = s.split(",")
            l.append(dict(zip(["name",'age','score'],ls)))
    except OSError:
        print("出了个什么错")
    finally: 
        file.close()
    return l 
def print_info(l):
    for d in l:
        print(d['name'],"今年",d['age'],'岁,成绩是:',d['score'])
lidt = read_info("lx1_info.txt")
print_info(lidt)


# myf = open("lx1_info.txt")
# myf1 = myf.readline()
# myf2 = tuple(myf1.split(","))
# print('%s今年%s岁,成绩是:%s' % (myf2),end="")
# myf3 = myf.readline()
# myf4 = tuple(myf3.split(","))
# print('%s今年%s岁,成绩是:%s' % (myf4),end="")
# myf5 = myf.readline()
# myf6 = tuple(myf5.split(","))
# print('%s今年%s岁,成绩是:%s' % (myf6),end="")












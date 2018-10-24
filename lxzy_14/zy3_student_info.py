def input_student(l):
    while True :
        # 让用户输入
        iname = input("Please input your name : ")
        # 如果输入为空则停止输入
        if iname == "":
            break
        iage = int(input("Please input your age : "))
        iscore = int(input("Please input your score : "))
        # 将字典存入列表
        l.append( dict(name = iname, age = iage, score = iscore))
    return l

# 给一个列表,使列表打印出来

def output_student(l):



    # 求最长
    max_wn = 4
    max_wa = 4
    max_ws = 4
    for i in l:
        h = len(i["name"])
        h2 = len(str(i["age"]))
        h3 = len(str(i["score"]))
        if h > max_wn:
            max_wn = h
        if h2 > max_wa:
            max_wa = h2
        if h3 > max_ws:
            max_ws = h3
    # print(max_wn) 



    print("+" + "-" * (max_wn+4)  + "+" +"-" * (max_wa+4)+ "+" + "-"*(max_ws+4) + "+")
    print("|"+"姓名".center(max_wn+2)+"|"+"年龄".center(max_wa+2)+"|"+"成绩".center(max_ws+2)+"|")
    print("+" + "-" * (max_wn+4)  + "+" +"-" * (max_wa+4)+ "+" + "-"*(max_ws+4) + "+")

    for i in l:
        # 拿出来
        bname = i['name']
        bage = str(i['age'])
        bscore = str(i['score'])
        # 判断输入的是否为汉子
        len_hz = 0
        for hz in bname:
            # 判断输入的名字中有没有汉子
            if ord(hz) > 128 :
                len_hz += 1
                continue
        
        print("|" + bname.center(max_wn-len_hz+4) + "|" + bage.center(max_wa+4) + "|" + bscore.center(max_ws+4) + "|")   
        print("+" + "-" * (max_wn+4)  + "+" +"-" * (max_wa+4)+ "+" + "-"*(max_ws+4) + "+")


# 定义一个函数用于删除列表中的字典

def rm_people(l):

    if l == []:
        print('没有学生信息,请按1输入')
        return
    rm_name = input("请输入您想删除谁的信息(如名字): ")
    for people in l:
        if rm_name == people["name"]:
            l.remove(people)
            print("删除成功")
            break
    else: 
        print("删除失败,没有您要删除的学生")


# 定义一个函数用于修改学生成绩

def mod_score(l):
    mod_name = input("您想修改谁的成绩: ")
   
    mod_name_score = int(input("您想修改{}的成绩为多少:".format(mod_name)))
    for people in l:
        # 判断想修改谁的
        if people["name"] == mod_name:
            # 开始修改
            people["score"] = mod_name_score
            print("修改成功")
    else:
        print("修改失败,没有您输入的学生")

# 定义一个函数用于成绩从高到低排序
# 用sorted 函数写
def score_high_low(l):
    def high(d):
        return d["score"]
    l = sorted(l , key = high , reverse = True)  
    # l.sort(key = high , reverse = True)
    print("排序成功")
    return l
# 定义一个函数用于成绩从低到高排序

def score_low_high(l):
    def low(d):
        return d["score"]
    l.sort(key=low)
    print("排序成功")
    
# 定义一个函数用于年龄从高到低排序

def age_high_low(l):
    def high(d):    
        return d["age"]
    l.sort(key = high , reverse = True)
    print("排序成功")   
    
# 定义一个函数用于年龄从低到高排序

def age_low_high(l):
    def low(d):
        return d["age"]
    l.sort(key=low)
    print("排序成功")

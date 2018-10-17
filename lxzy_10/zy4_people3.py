#   4. 实现带界面的学生信息管理程序
#     界面如下:
#     +----------------------+
#     | 1) 添加学生信息        |
#     | 2) 查看学生信息        |
#     | 3) 删除学生信息        |
#     | 4) 修改学生成绩        |
#     | q) 退出               |
#     +----------------------+
#     请选择:1
#     请输入学生姓名: xiaozhang
#     请输入学生年龄: 20

#     要求每个功能写一个函数与之相对应(复用之前的学生信息
#     管理程序)
   
# 定义一个函数 把每个学生信息以字典方式存入列表
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
        

def peo_itface():
    print("+----------------------+")
    print("| 1) 添加学生信息      |")
    print("| 2) 查看学生信息      |")
    print("| 3) 删除学生信息      |")
    print("| 4) 修改学生成绩      |")
    print("| q) 退出              |")
    print("+----------------------+")
    # 定义一个函数用于删除列表中的字典
    def rm_people(l):
        rm_name = input("请输入您想删除谁的信息(说如名字): ")
        for people in l:
            if rm_name == people["name"]:
                l.remove(people)
    # 定义一个函数用于修改学生成绩
    def mod_score(l):
        mod_name = input("您想修改谁的成绩: ")
        mod_name_score = int(input("您想修改{}的成绩为多少:".format(mod_name)))
        for people in l:
            # 判断想修改谁的
            if people["name"] == mod_name:
                # 开始修改
                people["score"] = mod_name_score


    while 1 :
        nub = input("请输入您想使用的功能对应的序号: ")
        # 添加
        if nub == "1":
            input_student(peoples)
            print("添加成功")
            output_student(peoples)
        # 查看
        elif nub == "2":
            output_student(peoples)
        # 删除
        elif nub == "3":
            rm_people(peoples)
            print("删除成功")
        # 修改成绩
        elif nub == "4":
            mod_score(peoples)
            print("修改成功")
            output_student(peoples)
        # 退出
        elif nub == "q":
            break
        else:
            print("请输入正确的选项")
            continue
# 定义一个空的列表用于存储用户数据
peoples = []
peo_itface()

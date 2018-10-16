#   2. 改写之前的学生信息管理程序,封装为两个函数:
#     def input_student():
#         # 此函数用于返回所有用户输入的学生信息的列表
#         ...
#     def output_studentn(L):
#         # 此函数以表格形式打印学生信息
#         ...
#     以下是调用(功能和打印效果与之前相同):
#     infos = input_student()
#     print(infos)
#     output_studentn(infos)


def input_student():
    p_book = []
    while True :
        # 让用户输入
        iname = input("Please input your name : ")
        # 如果输入为空则停止输入
        if iname == "":
            break
        iage = int(input("Please input your age : "))
        iscore = int(input("Please input your score : "))
        # 将字典存入列表
        p_book.append( dict(name = iname, age = iage, score = iscore))
    return p_book

def output_studentn(l):



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
        
    
l = input_student()
output_studentn(l)
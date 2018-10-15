# 4. 任意输入很多个学生的姓名,年龄，成绩,每个学生的信息  存入到字典中，然入再放在列表内
#     - 每个学生的信息需要手动输入:
#     - 如:  
#         请输入姓名: tarena  
#         请输入年龄: 15  
#         请输入成绩: 99  
#         请输入姓名: china  
#         请输入年龄: 70  
#         请输入成绩: 98  
#         请输入姓名: <回车>　结束输入  
#     内部存储格式如下:  
#     `infos = [{'name':'tarena', 'age':15, 'score':99}, 
#        {'name':'china', 'age':70, 'score':98}]`
#     1. 打印以上的列表
#     2. 按如下表格打印学生信息  
#     ```
#     +---------------+-----------+----------+  
#     |     姓名       |    年龄   |    成绩   |  
#     +---------------+-----------+----------+  
#     |    tarena     |     15    |    99    |  
#     |     china     |     70    |    98    |  
#     +---------------+-----------+----------+  
#     ```

# 第一步创建一个存储用户数据的列表
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
print(p_book)




# 求最长
max_wn = 4
max_wa = 4
max_ws = 4
for i in p_book:
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

for i in p_book:
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
    
    




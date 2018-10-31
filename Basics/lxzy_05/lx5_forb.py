s = "ABCDE"
for i in s :    
    if i == "D":
        break
    print(i)
else :
    print("for语句的else被执行")
print("结束")
# 在字符串不再有数据给遍历时，执行else
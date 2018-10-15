s1 = {"曹操", "刘备", "孙权"}
s2 = {"曹操", "张飞","关羽","孙权"}


s3 = s1 & s2
print("即是经理也是技术",s3)
s4 = s1 - s2
print("是经理不也是技术",s4)
s5 = s2 - s1
print("是技术不是经理",s5)
s6 = "张飞" in s1
print(s6)
s7 = s2 ^ s1
print("身兼一职",s7)
s8 = s1 | s2
print( "一共有",len(s8))


 
     
     
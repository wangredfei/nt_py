
def get_fun(s):
    def myadd(x, y):
        return x+y
    def mysub(x, y):
        return x-y
    def mymul(x, y):
        return x*y
    def myc(x, y):
        return x/y
    if s == "+":
        return myadd   
    if s == "-":
        return mysub
    if s == "*":
        return mymul
    if s == "/":
        return myc   
# 定义主函数
def main():
    while 1:
        s = input("输入计算公式")
        for i in s:
            if i == "+":
                L = s.split("+")
                break
            if i == "-":
                L = s.split("-")
                break
            if i == "*":
                L = s.split("*")
                break
            if i == "/":
                L = s.split("/") 
                break
        a = int(L[0])
        b = int(L[1])
        fn = get_fun(i)
        print("结果是: ",fn(a,b))
main()
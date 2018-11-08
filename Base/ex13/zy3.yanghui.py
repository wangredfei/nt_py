def get_yanghui_nextline(l):
    '''给定上一行列表生成下一行数的列表'''
    # l是这一行的列表
    # 定义下一行的列表
    # 这是开头的1
    rl = [1]
    for i in range(len(l)-1):
        rl.append(l[i]+l[i+1])   
    # 这是最后的1
    rl.append(1)
    return rl
# print(get_yanghui_nextline([1]))
def get_yanghui_lines(n):
    '''此函数输入n行数,返回[[1],[1,1],[1,2,1],....]'''
    # 定义返回列表
    rl = [[1]]
    # 调用生成下一行列表函数并加入到list中
    for i in range(n-1):
        rl.append(get_yanghui_nextline(rl[i]))
    return rl
# print(get_yanghui_lines(6))
def get_yanghui_str(l):
    '''此函数准备将
    [[1],[1,1],[1,2,1]]
    转换成
    ['1' , '1 1', '1 2 1']
    '''
    rl = []
    for line in l:
        line = ' '.join([str(x) for x in line])
        rl.append(line)
    return rl
# print(get_yanghui_str([[1], [1, 1], [1, 2, 1]]))

def main():
    try:
        n = int(input("请输入您想要的行数"))
    except:
        print("输入错误")
        return
    l = get_yanghui_lines(n)
    sl = get_yanghui_str(l)
    for line in sl:
        print(line.center(len(sl[-1])))
main()




# 打印菜单
def show_menu():
    print("+------------------------------------+")
    print("| 1) 添加学生信息                    |")
    print("| 2) 查看学生信息                    |")
    print("| 3) 删除学生信息                    |")
    print("| 4) 修改学生成绩                    |")
    print("| 5) 按学生成绩高-低显示学生信息     |")
    print("| 6) 按学生成绩低-高显示学生信息     |")
    print("| 7) 按年龄成绩高-低显示学生信息     |")
    print("| 8) 按年龄成绩低-高显示学生信息     |")
    print("| 9) 从文件中读取数据(si.txt)        |")
    print("|10) 保存信息到文件(si.txt)          |")
    print("| q) 退出                            |")
    print("+------------------------------------+")
if __name__ == "__main__":
    show_menu()
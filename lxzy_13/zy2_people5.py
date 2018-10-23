# 2. 修改原学生信息管理程序,将程序拆分为模块:
#    要求:
#      1. 主事件循环while语句放在main.py中
#      2. show_menu函数放在menu.py中
#      3. 与学生操作相关的函数放在student_info.py中
import zy2_show_menu as sm
import zy2_student_info as si
# 定义主函数
def main():
        
    peoples = []
    while 1 :
        # 调用菜单函数  
        sm.show_menu()
        nub = input("请输入您想使用的功能对应的序号: ")
        # 添加
        if nub == "1":
            si.input_student(peoples)
            print("添加成功")
        # 查看
        elif nub == "2":
            pass
        # 删除
        elif nub == "3":
            si.rm_people(peoples)
        # 修改成绩
        elif nub == "4":
            si.mod_score(peoples)
        # 按学生成绩从高到低排序
        elif nub == "5":
            peoples=si.score_high_low(peoples)
        # 按学生成绩从低到高排序
        elif nub == "6":
            si.score_low_high(peoples)    
        # 按年龄从低到高排序
        elif nub == "7":
            si.age_high_low(peoples)
        # 按年龄从高到低排序
        elif nub == "8":
            si.age_low_high(peoples)
        # 退出
        elif nub == "q":
            break
        else:
            si.print("请输入正确的选项")
            
        si.output_student(peoples)
        print("-"*50)
main()

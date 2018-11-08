# 示意F.write 和F.writelines
try :
    f = open("lx0_newfile.txt",'a') 

    f.write("不好\n")
    f.writelines("nishishabime")
    f.writelines("hahahaha")

    f.close()
except OSError:
    print("打开文件失败")
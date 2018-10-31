try:
    with  open("/home/tarena/nt_py/lxzy_20/myfile.txt") as fr:
        s = fr.read()
        print(s)
except OSError:
    print("文件打开失败")
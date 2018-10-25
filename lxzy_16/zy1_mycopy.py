#练习:
# 1. 写程序实现复制文件的功能
#     - 要求:
#        1. 要考虑超大文件问题
#        2. 要能复制二进制文件(如:图片等)
#        3. 要考虑关闭文件
def mycopy(old_file,newfile = 'newfile.txt'):
    try:
        of = open(old_file,'rb')
        nf = open(newfile,'wb')
        while 1 :
            of_code = of.read(100)
            nf.write(of_code)
            if of_code==b"":
                break
    except OSError:
        print("open file Error")
    finally:
        of.close()
        nf.close()
mycopy("a.jpg","hahaha.jpg")
mycopy("lx1_info.txt","commentcopy.txt")
    
# 三种布局
# pack 方位布局
# 默认从上到下,挨个放
# place 坐标布局
# grid 网络布局

import tkinter

base = tkinter.Tk()
lb1 = tkinter.Label(base,text="账号: ").grid(row=0,sticky=tkinter.W)
tkinter.Entry(base).grid(row=0, column=1, sticky=tkinter.E)
lb2 = tkinter.Label(base,text="密码: ").grid(row=1,sticky=tkinter.W)
tkinter.Entry(base).grid(row=1, column=1, sticky=tkinter.E)
lb1 = tkinter.Button(base,text="登录").grid(row=2, column=1, sticky=tkinter.W)
base.mainloop()
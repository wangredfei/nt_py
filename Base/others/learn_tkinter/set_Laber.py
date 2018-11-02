import tkinter

base = tkinter.Tk()
base.wm_title("Laber Test")
# 支持数次那个很多backgrond, font, underline等
# 第一个参数,制定所属
lb1 = tkinter.Label(base, text="python AI")
lb1.pack()
lb2 = tkinter.Label(base, text="绿色背景", background="green" )
lb2.pack()
lb3 = tkinter.Label(base, text="粉色背景", background="pink", font="宋体")
lb3.pack()
base.mainloop()
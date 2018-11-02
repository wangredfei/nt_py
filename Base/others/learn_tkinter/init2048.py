import tkinter as t

# 定义画布
root = t.Tk()
w = t.Canvas(root,width=100,height=100,background="green")
w.pack()
lb1 = t.Label(w,text="2",width=5, height=5, background="pink" ) 
lb1.grid(row=0, column=1,sticky=t.W)
# cav = root.frame()
# cav.pack()
root.mainloop()
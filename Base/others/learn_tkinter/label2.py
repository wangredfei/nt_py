import tkinter as t

root = t.Tk()

textlabel = t.Label(root, text="你好,\n么", justify="right",padx=10)
textlabel.pack(side="right")

t.mainloop()
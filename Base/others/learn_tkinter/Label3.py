import tkinter
root = tkinter.Tk()

# photo = tkinter.PhotoImage(file="a.jpg")
# ???
lb1 = tkinter.Label(root,
                    text="学习GUI",
                    justify="left",
                    image=photo,
                    compound="center",
                    font=("华康少女字体",20),
                    fg='black'
                    )


lb1.pack()
tkinter.mainloop()
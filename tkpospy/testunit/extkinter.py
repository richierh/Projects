import tkinter as tk

def login():
    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=0)
    root.title("Login")
    root.geometry("220x90+500+250")

    # make frame layout
    upframe = tk.Frame(root)
    upframe.grid(row=0,column=0,sticky=tk.EW)
    downframe = tk.Frame(root)
    downframe.grid(row=1,column=0,sticky=tk.E)

    upframe.grid_columnconfigure(1,weight=1)
    downframe.grid_columnconfigure(1,weight=1)
    downframe.grid_rowconfigure(2,weight=1)
    downframe.grid_columnconfigure(2,weight=1)

    #downframe.grid_rowconfigure(0,weight=1)

    lbl1=tk.Label(upframe,text="Nama")
    lbl2=tk.Label(upframe,text="Password")
    Etr1=tk.Entry(upframe,text="")
    Etr2=tk.Entry(upframe,text="")

    btn1=tk.Button(downframe,text="Button1")
    btn2=tk.Button(downframe,text="Button2")

    lbl1.grid(row=0,column=0,sticky=tk.W,pady = 3)
    lbl2.grid(row=1,column=0,sticky=tk.W,pady = 3)
    Etr1.grid(row=0,column=1,sticky=tk.EW,ipady=3)
    Etr2.grid(row=1,column=1,sticky=tk.EW,ipady=3)

    btn1.grid(row=0,column=0,pady=3,sticky=tk.NSEW)
    btn2.grid(row=0,column=1,pady=3,sticky=tk.NE)

root = tk.Tk()
login()
root.mainloop()

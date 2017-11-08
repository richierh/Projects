import Tkinter



def main():
    global Etr1
    return Etr1

def login():
    main()
    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=0)
    root.title("Login")
    root.geometry("220x90+500+250")

    # make frame layout
    upframe = Tkinter.Frame(root)
    upframe.grid(row=0,column=0,sticky=Tkinter.EW)
    downframe = Tkinter.Frame(root)
    downframe.grid(row=1,column=0,sticky=Tkinter.E)

    upframe.grid_columnconfigure(1,weight=1)
    downframe.grid_columnconfigure(1,weight=1)
    downframe.grid_rowconfigure(2,weight=1)
    downframe.grid_columnconfigure(2,weight=1)

    #downframe.grid_rowconfigure(0,weight=1)

    lbl1=Tkinter.Label(upframe,text="Nama")
    lbl2=Tkinter.Label(upframe,text="Password")
    Etr1=Tkinter.Entry(upframe)
    Etr2=Tkinter.Entry(upframe)

    btn1=Tkinter.Button(downframe,text="Button1",command=okay)
    btn2=Tkinter.Button(downframe,text="Button2",command=cancel)

    lbl1.grid(row=0,column=0,sticky=Tkinter.W,pady = 3)
    lbl2.grid(row=1,column=0,sticky=Tkinter.W,pady = 3)
    Etr1.grid(row=0,column=1,sticky=Tkinter.EW,ipady=3)
    Etr2.grid(row=1,column=1,sticky=Tkinter.EW,ipady=3)

    btn1.grid(row=0,column=0,pady=3,sticky=Tkinter.NSEW)
    btn2.grid(row=0,column=1,pady=3,sticky=Tkinter.NE)

def okay():
    print (Etr1.get())
    print ("okay")

def cancel():
    print ("cancel")
    root.destroy()



root = Tkinter.Tk()
login()
root.mainloop()

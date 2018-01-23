#! usr/bin/env python

import Tkinter as Tk
import ttk


class App():

    def __init__(self,*args,**kwds):
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.attributes('-zoomed')
        root.geometry("+100+300")

        Lframe = ttk.Frame(root)
        Rframe = ttk.Frame(root)
        #grid for main frame left and right , on column 0, and column 1

        Lframe.grid(row=0, column=0)
        Rframe.grid(row=0, column=1,sticky=Tk.E)
        Lframe.grid_rowconfigure(0, weight=1)
        Lframe.grid_columnconfigure(0, weight=1)
        #Rframe.grid_rowconfigure(0, weight=1)
        #Rframe.grid_columnconfigure(0, weight=1)
        Ruframe = ttk.Frame(Rframe)
        Rdframe = ttk.Frame(Rframe)
        Ruframe.grid(row=0, column =0, sticky = Tk.E)
        Rdframe.grid(row=0, column =0, sticky = Tk.E)
        # Layout Manager of Treeview inside it's parent
        Tree = ttk.Treeview(Rframe)

        Lblsearch = ttk.Label(Ruframe, text="Search")
        Lblsearch.grid(row=0, column = 1)
        Etrsearch = Tk.Entry(Ruframe,font = (None,12),width = 50)
        Etrsearch.grid(row=0, column=0,padx=5,ipady=5)
        
        Tree.grid(row=1, column=0, sticky =Tk.E)

        Tree["columns"]=["column2","column3","column4","column5"]

        Tree.heading("#0",text="No")
        Tree.column("#0",width=50,anchor= Tk.W)
        show=[]
        Tree.heading("column2", text="Nama Barang")
        Tree.heading("column3", text="Banyaknya")
        Tree.heading("column4", text="Harga Satuan")
        Tree.heading("column5", text="Harga Total")

        # Tree.insert()


root=Tk.Tk()
App()
root.mainloop()

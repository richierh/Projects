#!/usr/bin/env python

import tkinter as Tk
from tkinter import ttk

class App(Tk.Tk):

	def __init__(self):
		self.root=Tk.Tk()
		self.root.grid_rowconfigure(0,weight=1)
		self.root.grid_columnconfigure(0,weight=1)
		self.root.geometry("800x300+200+200")
		self.root.title("Aplikasi Python POS Lite")
		"""
		Frame Top
		"""
		self.FrameT = Tk.Frame(self.root, height = 200 , width = 500)
		self.FrameT.grid(row=0, column=0,sticky="nsew")
		self.FrameT.grid_rowconfigure(0,weight=0) # Membuat layout judul tidak Growable
		self.FrameT.grid_rowconfigure(1,weight=0)
		self.FrameT.grid_rowconfigure(2,weight=1)

		self.FrameT.grid_columnconfigure(0,weight=1)

		"""
		Frame Judul
		"""
		
		self.FrameJdl= Tk.Frame(self.FrameT)
		self.FrameJdl.grid(row=0, column=0, sticky="nsew")
		self.FrameJdl.grid_columnconfigure(0,weight=1)
		self.FrameJdl.grid_rowconfigure(0,weight = 1)
		
		self.Label = Tk.Label(self.FrameT, text = "INPUT DATA", font=("liberation Sans",20),anchor="c")
		self.Label.grid(row=0,column=0, sticky = "nsew")
		

		"""
		Frame Atas 1
		"""
		self.FrameA1 = Tk.Frame(self.FrameT)
		self.FrameA1.grid(row=1, column=0,sticky="nsew")
		
		self.FrameA1.grid_rowconfigure(5,weight=0)
		#self.FrameA1.grid_rowconfigure(0,weight=1)
		self.FrameA1.grid_columnconfigure(1,weight=1)


		"""
		#Etr1value = Tk.StringVar(self.FrameA1,value = "Harap dimasukkan Datanya")

		self.Label2= Tk.Label(self.FrameA1,text = "ID Produk",anchor="w")
		self.Label2.grid(row=1, column = 0,sticky="nsew")
		self.Etr2 = Tk.Entry(self.FrameA1,text ="Entry1")#,textvariable=Etr1value)
		self.Etr2.grid(row=1,column=1,sticky="nsew")

		self.Label3= Tk.Label(self.FrameA1,text = "Nama Barang",anchor="w")
		self.Label3.grid(row=2, column = 0,sticky="nsew")
		self.Etr3 = Tk.Entry(self.FrameA1,text ="Entry2")#,textvariable=Etr1value)
		self.Etr3.grid(row=2,column=1,sticky="nsew")

		self.Label4= Tk.Label(self.FrameA1,text = "Kuantiti",anchor="w")
		self.Label4.grid(row=3, column = 0,sticky="nsew")
		self.Etr4 = Tk.Entry(self.FrameA1,text ="Entry3")#,textvariable=Etr1value)
		self.Etr4.grid(row=3,column=1,sticky="nsew")

		self.Label5= Tk.Label(self.FrameA1,text = "Harga Produk",anchor="w")
		self.Label5.grid(row=4, column = 0,sticky="nsew")
		self.Etr5 = Tk.Entry(self.FrameA1,text ="Entry4")#,textvariable=Etr1value)
		self.Etr5.grid(row=4,column=1,sticky="nsew")
		"""

		listtext=["No","ID Produk","Nama Barang","Kuantiti","Harga Produk","Informasi Tambahan"]
		
		for col in range(1,len(listtext)-1):
			#print (col)
			self.Label = Tk.Label(self.FrameA1,text ="{}".format(listtext[col]),anchor="w")
			self.Label.grid(row=col,column=0,sticky="nsew")
			self.Etr = Tk.Entry(self.FrameA1,text ="Entry{}".format(col+1),state="normal")
			self.Etr.grid(row=col,column=1,sticky="nsew")

		self.Etr1 = Tk.Entry(self.FrameA1,text ="Entry",state="disabled")
		self.Etr1.grid(row=0,column=1,sticky="w")#atur panjang Entry No
		self.Label1= Tk.Label(self.FrameA1,text = "No",anchor="w")
		self.Label1.grid(row=0, column = 0,sticky="nsew")
		
		self.Label6= Tk.Label(self.FrameA1,text = "Informasi Tambahan",anchor="w")
		self.Label6.grid(row=5, column = 0,sticky="nsew")
		self.Etr6 = Tk.Text(self.FrameA1,height=2)#,text ="Entry1")#,textvariable=Etr1value)
		self.Etr6.grid(row=5,column=1,sticky="nsew")
	


		"""
		Frame Atas 1 Kanan untuk button
		"""
		self.FrameA1one=Tk.Frame(self.FrameA1)
		self.FrameA1one.grid(row=6,column=1,sticky="e")
		self.FrameA1one.grid_columnconfigure(0,weight=1)
		self.FrameA1one.grid_columnconfigure(1,weight=1)

		self.Button1 = Tk.Button(self.FrameA1one,text = "Ok",height=2,padx=70)
		self.Button2 = Tk.Button(self.FrameA1one,text = "Batal",height=2,padx=70)

		self.Button1.grid(row=0,column=0,sticky="e",pady=3)
		self.Button2.grid(row=0, column=1, sticky="e",pady=3)

		"""
		Frame Atas 2
		"""
		self.FrameA2 = Tk.Frame(self.FrameT)
		self.FrameA2.grid(row=2, column=0,sticky="nsew")
		self.FrameA2.grid_rowconfigure(0,weight=1)
		self.FrameA2.grid_columnconfigure(0,weight=1)

		self.treeview = ttk.Treeview(self.FrameA2)
		self.treeview["columns"]=["ID","Produk","Stok","Harga","Informasi Tambahan"]
		self.treeview["show"]=["headings"]
		
		for colid in range(0,len(self.treeview["columns"])):
			self.treeview.heading("{}".format(self.treeview["columns"][colid]),text="{}".format(self.treeview["columns"][colid]))
			#print (len(self.treeview["columns"]))#[1])
		
		self.treeview.heading("ID",text="ID")
		self.treeview.grid_rowconfigure(0,weight=1)
		self.treeview.grid_columnconfigure(0,weight=1)
		self.treeview.grid(row=0,column=0,sticky="nsew")

	def mainloop(self):
		self.root.mainloop()


if __name__=="__main__":
	K = App()
	K.mainloop()

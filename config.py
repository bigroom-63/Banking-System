#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk,messagebox,filedialog
from datetime import datetime
#				C
import otp_handler
import acc_gen
import json_handler
import close_acc
import tree
#				o
import txn
import json
import os
import copy
#				d
root=Tk()
root.geometry('2000x1000')
root.title('Banking App')

root.grid_rowconfigure(0,weight=1)
#				e
root.grid_columnconfigure(0,weight=1)

notebook=ttk.Notebook(root)
tab1=ttk.Frame(notebook)
tab2=ttk.Frame(notebook)
#				d
tab3=ttk.Frame(notebook)
tab4=ttk.Frame(notebook)
notebook.add(tab1,text='Create New Account')
notebook.add(tab2,text='Close Account')
notebook.add(tab3,text='Offline Transaction')
#				b
notebook.add(tab4,text='Data')
notebook.grid(row=0,column=0,sticky='nsew')
rows=16
columns=8
tab1.grid_rowconfigure(15,weight=1)
#				y
tab1.grid_columnconfigure(7,weight=1)

def kill():
	root.destroy()

kill_but=Button(root,text='Done',command=kill)
#				B
kill_but.grid(row=15,column=7,sticky='se',padx=10,pady=10)

def link4():
	tree.table1(tab4,notebook)
#				I
tree_but=Button(root,text='Check Account Info',command=link4)
tree_but.grid(row=14,column=7,sticky='se',padx=10,pady=10)

l1=Label(tab1,text='Full Name',fg='magenta',bg='green',font=('OCRA',9,'bold')).grid(row=1,column=0,sticky='w')
#				K
l2=Label(tab1,text='Address',fg='magenta',bg='green',font=('OCRA',9,'bold')).grid(row=2,column=0,sticky='w')
l3=Label(tab1,text='Contact',fg='magenta',bg='green',font=('OCRA',9,'bold')).grid(row=3,column=0,sticky='w')
l4=Label(tab1,text='Initial Deposit',fg='magenta',bg='green',font=('OCRA',9,'bold')).grid(row=4,column=0,sticky='w')

e1=Entry(tab1,borderwidth=5)
#				R
e2=Entry(tab1,borderwidth=5)
e3=Entry(tab1,borderwidth=5)
e4=Entry(tab1,borderwidth=5)

e1.grid(row=1,column=1)
#				A
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)

def otp():
#				M
	gen_otp=otp_handler.otp_gen()
	l5=Label(tab1,text='OTP:',fg='magenta',bg='green',font=('OCRA',9,'bold'))
	l5.grid(row=5,column=0,sticky='w')
	e5=Entry(tab1,borderwidth=5)
	e5.grid(row=5,column=1)
#				B
	messagebox.showinfo('OTP',gen_otp)
	print(gen_otp)
	def get_otp():
		ent_otp=e5.get()
		if ent_otp!=gen_otp:
#				H
			messagebox.showerror('Error','OTP mismatch,Please retry')
		l6=Label(tab1,text='4 Digit Pincode:',fg='magenta',bg='green',font=('OCRA',9,'bold'))
		l6.grid(row=6,column=0,sticky='w')
		e6=Entry(tab1)
		e6.grid(row=6,column=1)
#				A
		def get_acc():
			acc={}
			acc['name']=e1.get()
			acc['address']=e2.get()
			acc['contact']=e3.get()
#				T
			acc['balance']=float(e4.get())
			acc['pincode']=e6.get()
			acc['acc_no']=acc_gen.get_acc()
			acc['card_no']=acc_gen.get_card()
			current_datetime=datetime.now()
#				T
			acc['txn_date']=current_datetime.strftime('%Y-%m-%d %H:%M:%S')
			acc['txn_type']='Deposit'
			acc['txn_amt']=float(e4.get())
			data=json_handler.read_rec()
#				A
			for rec in data:
				if acc['contact']==rec['contact']:
					messagebox.showerror('Account already exists',f"Account already exist with contact no {rec['contact']}")
				break
			data.append(copy.deepcopy(acc))
#				R
			sorted_data=sorted(data,key=lambda x:datetime.strptime(x['txn_date'],'%Y-%m-%d %H:%M:%S'))
			create_but.destroy()
			pin_but.destroy()
			l5.destroy()
			l6.destroy()
#				A
			e5.destroy()
			e6.destroy()
			e1.delete(0,END)
			e2.delete(0,END)
#				I
			e3.delete(0,END)
			e4.delete(0,END)
			json_handler.update(data)
			messagebox.showinfo('Success',f"New account with account number {acc['acc_no']} created")
		create_but=Button(tab1,text='Create',command=get_acc)
		create_but.grid(row=3,column=2,sticky='e',padx=20)
	pin_but=Button(tab1,text='OTP Submit',command=get_otp)
	pin_but.grid(row=2,column=2,sticky='e',padx=20)
otp_but=Button(tab1,text='Submit',command=otp)
otp_but.grid(row=1,column=2,sticky='e',padx=20)

close_acc.link(tab2)

txn.txn(tab3,tab4,notebook)

root.mainloop()


#coded by : Bikram Bhattarai

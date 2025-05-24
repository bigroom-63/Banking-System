from tkinter import Label,Entry,Button,messagebox
from datetime import datetime
import json_handler

def link(tab2):
	la2=Label(tab2,text='Account Number:',fg='magenta',bg='green',font=('OCRA',10,'bold'))
	la2.grid(row=1,column=0,sticky='w')
	en2=Entry(tab2,borderwidth=5)
	en2.grid(row=1,column=1)
	def get_acc():
		match_acc_no=en2.get().strip().replace(' ','')
		data=json_handler.read_rec()
		account=max((acc for acc in data if acc['acc_no'].replace(' ','')==match_acc_no),key=lambda acc:datetime.strptime(acc['txn_date'],'%Y-%m-%d %H:%M:%S'),default=None)
		if not account:
			messagebox.showerror('Error','Account not found')
		filtered=[]
		for acc in data:
			if acc!=account and acc['acc_no']!=account['acc_no']:
				filtered.append(acc)
		print(filtered)
		json_handler.update(filtered)
		messagebox.showinfo('Account Closed',f"Account {account['acc_no']} has been closed with refund of balance {account['balance']}.Thank You for Banking with us")

	get_but=Button(tab2,text='Submit',command=get_acc)
	get_but.grid(row=1,column=3)


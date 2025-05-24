import tkinter
import copy
from tkinter import messagebox,Entry,Label,Button,simpledialog
from datetime import datetime
import json_handler
import tree

def txn(tab3,tab4,notebook):
	la3=Label(tab3,text='Account Number:',fg='magenta',bg='green',font=('OCRA',9,'bold'))
	la3.grid(row=1,column=0,sticky='w')
	en3=Entry(tab3,borderwidth=5)
	en3.grid(row=1,column=1)
	def get_acc():
		match_acc_no=en3.get().strip().replace(' ','')
		data=json_handler.read_rec()
		record=max((acc for acc in data if acc['acc_no'].replace(' ','')==match_acc_no), key=lambda acc:datetime.strptime(acc['txn_date'],'%Y-%m-%d %H:%M:%S'),default=None)
		print(record)
		if not record:
			messagebox.showerror('Error','Account not found')
			return

		choice=simpledialog.askstring(title='Options',prompt=f"Dear {record['name']} Enter your Choice\n1-Deposit\n2-Withdraw\n3-Check Balance\n4-Show transaction history")
		match choice:
			case '1':
				la31=Label(tab3,text='Deposit Amount:',fg='magenta',bg='green',font=('OCRA',9,'bold'))
				la31.grid(row=2,column=0)
				en31=Entry(tab3,borderwidth=5)
				en31.grid(row=2,column=1)
				def deposit():
					record_copy=copy.deepcopy(record)
					record_copy['txn_amt']=float(en31.get())
					record_copy['balance'] +=record_copy['txn_amt']
					record_copy['txn_type']='Deposit'
					current_datetime=datetime.now()
					record_copy['txn_date']=current_datetime.strftime('%Y-%m-%d %H:%M:%S')
					la31.destroy()
					en31.destroy()
					dep_but.destroy()
					data.append(copy.deepcopy(record_copy))
					print(data)
					temp=json_handler.update(data)
					d=json_handler.read_rec()
					messagebox.showinfo('Success','Transaction recorded')
				dep_but=Button(tab3,text='Submit',command=deposit)
				dep_but.grid(row=2,column=3)
			case '2':
				la32=Label(tab3,text='Withdraw Amount:',fg='magenta',bg='green',font=('OCRA',9,'bold'))
				la32.grid(row=2,column=0)
				en32=Entry(tab3,borderwidth=5)
				en32.grid(row=2,column=1)
				def withdraw():
					record_copy=copy.deepcopy(record)
					record_copy['txn_amt']=float(en32.get())
					if record_copy['txn_amt']>record['balance']:
						messagebox.showerror('Error','Insufficient fund,please enter valid amount')
						record_copy['txn_amt']=0.0
					else:
						record_copy['balance'] -=record_copy['txn_amt']
						record_copy['txn_type']='Withdraw'
						current_datetime=datetime.now()
						record_copy['txn_date']=current_datetime.strftime('%Y-%m-%d %H:%M:%S')
						la32.destroy()
						en32.destroy()
						dep_but.destroy()
						data.append(copy.deepcopy(record_copy))
						json_handler.update(data)
						messagebox.showinfo('Success','Transaction recorded')
				dep_but=Button(tab3,text='Submit',command=withdraw)
				dep_but.grid(row=2,column=3)
			case '3':
				messagebox.showinfo('Balance Check',f"Dear {record['name']} your current balance is {record['balance']}")
			case '4':
				print(record)
				acc=record['name']
				filtered_data=list(filter(lambda txn:txn['name']==acc,data))
				transformed_data=[{k:v for k,v in d.items() if k not in ['address','contact','pincode','card_no']} for d in filtered_data]
				for item in transformed_data:
					item['balance']=item.pop('balance')
				sorted_data=sorted(transformed_data,key=lambda x: datetime.strptime(x['txn_date'],'%Y-%m-%d %H:%M:%S'))
				tree.table2(tab4,notebook,sorted_data)
			case _:
				messagebox.showerror('Error','Invalid Choice')
	get_but=Button(tab3,text='Submit',command=get_acc)
	get_but.grid(row=1,column=3)

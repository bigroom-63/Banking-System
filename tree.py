from tkinter import ttk
from datetime import datetime
import json_handler
import export

def kill_widget(tab):
	for widget in tab.winfo_children():
		widget.destroy()

def create_table(tab4,notebook,data):
	kill_widget(tab4)
	notebook.select(tab4)
	if not data:
		return
	columns=list(data[0].keys())
	style=ttk.Style()
	style.configure('Treeview',rowheight=30)
	tree=ttk.Treeview(tab4,columns=columns,show='headings',height=15)
	for col in columns:
		tree.heading(col,text=col)
		tree.column(col,width=100,anchor='center')
	for entry in data:
		values=[entry[key] for key in columns]
		tree.insert('','end',values=values)
	tree.grid(row=0,column=0,sticky='nsew')
	tab4.grid_rowconfigure(0,weight=1)
	tab4.grid_columnconfigure(0,weight=1)
	scrollbar1=ttk.Scrollbar(tab4,orient='vertical',command=tree.yview)
	tree.configure(yscrollcommand=scrollbar1.set)
	scrollbar1.grid(row=0,column=1,sticky='ns')

	def copy_to_clipboard(event=None):
		selected_item=tree.focus()
		value=tree.item(selected_item,'values')
		if value:
			tab4.clipboard_clear()
			tab4.clipboard_append(value[5])
			tab4.update()
	tree.bind('<Control-c>',copy_to_clipboard)

	def exp():
		export.save(tree)
	exp_but=ttk.Button(tab4,text='Export',command=exp)
	exp_but.grid(row=1,column=11)

def table1(tab4,notebook):
	data=json_handler.read_rec()
	sorted_data=sorted(data,key=lambda x: datetime.strptime(x['txn_date'],'%Y-%m-%d %H:%M:%S'))
	create_table(tab4,notebook,sorted_data)

def table2(tab4,notebook,filtered_data):
	create_table(tab4,notebook,filtered_data)


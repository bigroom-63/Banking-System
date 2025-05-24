import csv
from tkinter import filedialog,messagebox

def save(tree):
	filename=filedialog.asksaveasfilename(defaultextension='.csv',filetypes=[('CSV Files','*.csv'),('All Files','*.*')],title='Save CSV File')
	if not filename:
		return
	with open(filename,mode='w',newline='',encoding='utf-8') as file:
		writer=csv.writer(file)

		columns=[tree.heading(col)['text'] for col in tree['columns']]
		writer.writerow(columns)

		for row in tree.get_children():
			values=tree.item(row)['values']
			writer.writerow(values)

	messagebox.showinfo('Success',f'Data Successfully Exported to {filename}')

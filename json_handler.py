import json
import os
from tkinter import messagebox

filename='/home/bikram/bank/master_date.json'
def update(data):
	if not os.path.exists:
		messagebox.showerror('Error','File does not exists')
		return
	try:
		with open(filename,'w') as f:
			json.dump(data,f,indent=4)
#		messagebox.showinfo('Done','Account data updated')
	except Exception as e:
		messagebox.showerror('Error','Record does not exist.Error: {str(e)}')

def read_rec():
	if not os.path.exists(filename):
		return []
	try:
		with open(filename,'r') as f:
			return json.load(f)
	except (FileNotFoundError,json.JsonDecodeError):
		messagebox.showerror('Error',f'file {filename} contains invalid JSON.Returning an empty list')
		return []
	except Exception as e:
		messagebox.showerror('Error',f'An error occurred while reading the file {e}')
		return []

def create_acc(acc):
	data=read_rec()
	for record in data:
		if record['contact']==acc['contact']:
			messagebox.showerror('Error',f"{acc['contact']} is already registered")
			return False
		data.append(acc)
		update(data)



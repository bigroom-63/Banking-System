import datetime
def get_acc():
	now=str(datetime.datetime.now())
	accno=now[0:4]+' '+now[5:7]+now[8:10]+' '+now[11:13]+now[14:16]+' '+now[17:19]+now[20:22]
	return accno

def get_card():
	accno=get_acc()
	cardno=accno[10:]
	return cardno


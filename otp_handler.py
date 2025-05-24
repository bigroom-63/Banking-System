import secrets
import string

def otp_gen():
	otp=''
	o=string.digits
	for i in range(6):
		num=secrets.choice(o)
		otp+=num
	return otp




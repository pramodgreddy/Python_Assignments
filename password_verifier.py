import string

# val=[abcdefghijklmnopqrsdtuvwxyz]
# uppercase_val=val.uppper()
username=input("enter your email id: ")
check=username.split("@")
count_upper=0
count_lower=0
count_digits=0
count_sym=0
# print(check)
if(check[1].lower()!="gmail.com"):
	print("Invalid Username:")
else:
	print("Your Username is verified \n")
	print("*"*40)

	password=input("Enter your password: ")
	# lower=list(string.ascii_lowercase)
	# upper=list(string.ascii_uppercase)
	for i in password:
		if (ord(i)>=65 and ord(i)<=90):
			# if(ord(i)>=97 and ord(i)<=122):
			count_upper+=1
			# print(count_upper)
		if((ord(i)>=97 and ord(i)<=122)):
			count_lower+=1
		
		if(ord(i)>=48 and ord(i)<=57):
			count_digits+=1
		if(ord(i)==35 or ord(i)==36 or ord(i)==64):
			count_sym+=1

	# print(count_upper,count_lower,count_digits,count_sym)
	if(count_lower>0 and count_upper>0 and count_digits>0 and count_sym>0 and (len(password)>8) and (len(password)<16)):
		print("password is good!")



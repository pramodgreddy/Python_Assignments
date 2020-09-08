import datetime
from parking import Parking

p1=Parking(50,25)
# b1.book_parking_slot()
# b1.unbook_parking_slot()
list_2_wheeler_number=[]
list_4_wheeler_number=[]



def book_slot():

	print("which vehicle do you need to park?\n")
	print("*"*40)
	print("Enter 1 for 2 wheeler: \n")
	print("Enter 2 for 4 wheeler: \n")
	check=int(input("Enter your choice: \n "))
	print("*"*40)
	if(check==1):
		
		vehicle_number=input("Enter the 2 wheeler's License plate number: ")
		list_2_wheeler_number.append(vehicle_number)	
		p1.book_2_wheeler_slot()

	elif(check==2):
		
		vehicle_number=input("Enter the 4 wheeler's License plate number: ")
		list_4_wheeler_number.append(vehicle_number)	

		p1.book_4_wheeler_slot()

def unbook_slot():
	print("which vehicle do you need to unbook? \n")
	print("*"*40)
	print("Enter 1 for 2 wheeler: \n")
	print("Enter 2 for 4 wheeler: \n")
	check=int(input("Enter your choice:  "))
	if(check==1):
		l_check=input("Enter the 2 wheeler's License plate number to be unbooked: \n")
		for i in list_2_wheeler_number:
			if i==l_check:
				print("you can now unbook the 2 wheeler vehicle\n")
				p1.unbook_2_wheeler_slot()
			else:
				print("License plate number invalid\n")

	elif(check==2):
		l_check=input("Enter the 4 wheeler's License plate number to be unbooked: \n")
		for i in list_4_wheeler_number:
			if i==l_check:
				print("you can now unbook the 4 wheeler vehicle\n")
				p1.unbook_4_wheeler_slot()

			else:
				print("License plate number invalid\n")


while(True):
	print("HELLO Welcome to the parking lot\n")
	park_val=int(input("Enter 1 to book a slot  \nEnter 2 to unbook a slot \nEnter 3 to exit \n"))
	print("*"*40)
	if (park_val==1):
		book_slot()
	elif (park_val==2):
		unbook_slot()
	elif (park_val==3):
		break






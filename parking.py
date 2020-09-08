import datetime

class Parking:
	def __init__(self,two_wheeler_slots,four_wheeler_slots):
		self.two_wheeler_slots=two_wheeler_slots
		self.four_wheeler_slots=four_wheeler_slots


	def book_2_wheeler_slot(self):
		# self.vehicle_type=""
		# vehicle_type=input(" enter '2 wheeler' for a 2 wheeler or '4 wheeler' for a car: ")
		# self.vehichle_number=""
		# if vehicle_type=="2 wheeler":
		self.two_wheeler_slots-=1
		if(self.two_wheeler_slots>=0):
			self.record_in_time=datetime.datetime.now()
			print(f"The entry time for your two wheeler is: {self.record_in_time}\n ")
			print(f"Total 2 wheeler slots left is: {self.two_wheeler_slots}\n")
			print("*"*40)
		else:
			pass


	def book_4_wheeler_slot(self):


		# elif vehicle_type=="4 wheeler":
		self.four_wheeler_slots-=1
		if(self.four_wheeler_slots>=0):
			self.record_in_time=datetime.datetime.now()
			print(f"The entry time for your four wheeler is: {self.record_in_time}\n")
			print(f"Total CAR slots left is: {self.four_wheeler_slots}\n")
			print("*"*40)	

		else:
			pass			


	def unbook_2_wheeler_slot(self):
		# self.vehicle_type=""
		# vehicle_type=input(" Enter '2 wheeler' for a 2 wheeler  EXIT  or \n '4 wheeler' for a car EXIT : ")
		# if vehicle_type=="2 wheeler":
		self.two_wheeler_slots+=1
		if(self.two_wheeler_slots>=0 ):
			self.record_out_time=datetime.datetime.now()
			print(f"The exit time for the two wheeler slots is: {self.record_out_time}\n")
			print(f"total 2 wheeler slots left is: {self.two_wheeler_slots}\n")
			print("*"*40)
			total_tim=self.record_out_time -self.record_in_time
			total_time=total_tim.total_seconds()
			print("*"*40)
			print(f"total time parked: {total_time}")
			print("*"*40)
			price=(total_time*0.01)
			print(f"total price for {total_time} seconds is {price}")
		else:
			pass

	def unbook_4_wheeler_slot(self):		

		# elif vehicle_type=="4 wheeler":
		self.four_wheeler_slots+=1
		if(self.four_wheeler_slots>=0):
			self.record_out_time=datetime.datetime.now()
			print(f"The exit time for the four wheeler slots is: {self.record_out_time} \n ")
			print(f"total CAR slots left is: {self.four_wheeler_slots}\n")
			print("*"*40)
			total_tim=self.record_out_time -self.record_in_time
			total_time=total_tim.total_seconds()
			print("*"*40)
			print(f"total time parked: {total_time}")		
			print("*"*40)
			price=(total_time*0.02)
			print(f"total price for {total_time} seconds is {price}")

		else:
			pass





b1=Parking(50,25)
# b1.book_2_wheeler_slot()
# b1.book_4_wheeler_slot()
# b1.unbook_2_wheeler_slot()
# b1.unbook_4_wheeler_slot()




		



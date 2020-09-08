class Account:
	def __init__(self,name,ph_no,acc_no,bal):
		self.name=name
		self.phone=ph_no
		self.account=acc_no
		self.bal=bal

	def deposit(self,dep_val):
		self.bal+=dep_val

	def withdrawl(self,draw_val):
		self.bal-=draw_val

	def bal_check(self):
		print(self.bal)

a1=Account("pramod",85533,12345,500)
a1.bal_check()
a1.deposit(100)
a1.bal_check()
a1.withdrawl(50)
a1.bal_check()
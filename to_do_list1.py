class ToDoList1:
	def __init__(self,name,to_do=[],done=[]):
		self.name=name
		self.to_do=to_do
		self.done=done


	def add_task(self):
		# self.to_do=[]
		# print("enter a new task to be added to your list!")
		self.name=input("enter the name of your todo list! \n")
		for i in range(10):
			ele=input("enter a new task! or Enter 'exit' to exit \n")
			if(ele.lower()=="exit"):
				break
			else:
				self.to_do.append(ele)
		print("*"*40)   
		print(f"{self.name} list contains {self.to_do}\n")


	def mark_done(self):
		print(self.to_do)
		val=int(input("enter the index of the task that is be marked done!"))
		for i in self.to_do:
			if val==self.to_do.index(i):
				self.done.append(i)
				self.to_do.remove(i)
	
	def see_tasks(self):
		print(f"The {self.name} has now been updated\n ")
		print(self.to_do)
		print("*"*40)
		print("The marked done list consists:\n")
		print(self.done)





t1=ToDoList1("grocery list")
t1.add_task()
t1.mark_done()
t1.see_tasks()






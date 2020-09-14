

def nth_lowest():

	list1=[]
	val=int(input("enter the size of the list: "))
	for i in range(val):
		state=int(input("enter the list items"))
		list1.append(state)

	main_list=sorted(list1)
	print(main_list)
	repeted=[]

	for j in main_list:
		if j not in repeted:
			repeted.append(j)
	print(repeted)

	number=int(input("enter which nth_lowest number required! \n"))

	print(f"the {number} th lowest element in the list is: ")
	print(repeted[number-1])



nth_lowest()


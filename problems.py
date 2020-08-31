
#Print all the elements less than 5
# def print_less():
	
# 	list1=[1,1,2,3,5,6,12,24,56]
# 	list2=[]
# 	for input1 in list1:
# 		print(input1)
# 		if(input1<5):
# 			list2.append(input1)
# 	print(list2)



# print_less()


#Search the list for the element
# def search():
# 	list1=[1,2,3,2,0,65,21,4,2,10]
# 	list2=[]

# 	for i,j in enumerate(list1):
# 		if(j==2):
# 			list2.append(i)

# 	print(list2)

# search()




#eliminate duplicates in a list
# def eliminate_dup():
# 	list1=[1,1,2,3,4,64,35,93,35,87,4,3]
# 	list2=[]

# 	for i in list1:
# 		if i not in list2:
# 			list2.append(i)

# 	print(list2)

	
# eliminate_dup()


def reverse():
	str1=input("enter a string: ")
	print(f"string is {str1}")
	str2=""
	str1.lower()
	str1.split(" ")
	str1=str1.split()[::-1]
	str2=' '.join(str1)
	str2=str2.capitalize()
	print(str2)
	


reverse()




import pprint 
def word_count():
	val=input("enter the sentence: \n")
	check_list=sorted(list(val.split(" ")))
	print(check_list)
	# check_list=sorted(check_list1)
	l_size = len(check_list) 
	repeated = [] 
	dict1={}
	
	for i in range(l_size): 
		k = i + 1
		count=0
		for j in range(l_size): 
			if (check_list[i] == check_list[j]):
				count+=1
				

		dict1[check_list[i]]=count
			

	pprint.pprint(dict1)            



word_count()